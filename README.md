# Kedi-mama-takip
Kedinizin mama kabını takip etmek için Python ve OpenCV kullanarak geliştirilmiş bir uygulama
# Kedi Mama Takip

Kedi Mama Takip, kedinizin mama kabını takip etmek için Python ve OpenCV kullanarak geliştirilmiş bir uygulamadır. Bu uygulama sayesinde, kedinizin mama kabının dolu olup olmadığını kontrol edebilir ve mama kabı boş olduğunda e-posta ile uyarı alabilirsiniz.

## Gereksinimler

- Python 3.x
- OpenCV
- winsound (Windows için)
- yagmail

## Kurulum

1. Projeyi GitHub'dan indirin veya klonlayın:

git clone https://github.com/kullaniciadiniz/kedi-mama-takip.git

2. Gerekli Python paketlerini yükleyin:

pip install opencv-python yagmail

## Kullanım

3. `kedi-mama-takip.py` dosyasını açın ve aşağıdaki alanları doldurun:

gmail_user = "gönderenin email adresi"
gmail_password = "gönderenin mail şifresi"
to = "alıcı email adresi"


4. Uygulamayı çalıştırın:

python kedi-mama-takip.py


Uygulama çalıştığında, kedinizin mama kabının dolu olup olmadığını kontrol eder ve eğer boşsa belirtilen e-posta adresine uyarı gönderir.

## Lisans

Bu proje, MIT Lisansı ile lisanslanmıştır. Daha fazla bilgi için [LICENSE](LICENSE) dosyasını inceleyin.





