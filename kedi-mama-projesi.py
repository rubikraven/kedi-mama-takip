import cv2
import winsound
import yagmail

# E-mail
gmail_user = "gönderenin email adresi"
gmail_password = "gönderenin mail şifresi"

# E-mail alıcı
to = "alıcı email adresi"
subject = "Kedinizin maması bitti"
body = "Lütfen kedinizin mamasını yenileyiniz."


max_emails = 3


webcam = cv2.VideoCapture(0)

# mama kabı koordinat
x1, y1, x2, y2 = 50, 50, 200, 200


mail_count = 0

while True:
    # Read images
    success, frame = webcam.read()


    cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 255), 2)


    food_bowl = cv2.cvtColor(frame[y1:y2, x1:x2], cv2.COLOR_BGR2GRAY)


    avg_gray_level = food_bowl.mean()


    if avg_gray_level > 50:
        print("Mama kabı boş")
        # kab bos ses cal
        winsound.Beep(2000, 500)


        if mail_count < max_emails:
            yag = yagmail.SMTP(gmail_user, gmail_password)
            yag.send(to=to, subject=subject, contents=body)

            
            mail_count += 1
    else:
        print("Mama kabı dolu")


    cv2.putText(frame, f"Mail count: {mail_count}/{max_emails}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

    cv2.imshow("Webcam", frame)


    if cv2.waitKey(1) & 0xFF == ord("q"):
        break


webcam.release()
cv2.destroyAllWindows()
