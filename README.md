# Yaşayan Sözlük – animasyonlu sayfalar

Her isim için bir animasyon sayfası (`public/<isim>/`). Render.com'da "Static Site" olarak yayınlanır (render.yaml hazır).

QR kodlarını yeniden üretmek için (site adresi belli olunca):

    pip install qrcode pillow
    python3 build.py https://SITE-ADRESI.onrender.com

QR'lar `qr/` klasörüne yazılır; `TUM_QR_KODLARI_A4.pdf` tek sayfada hepsini içerir.
