from menu_sistemi import Menu

# Örnek fonksiyonlar
def kitap_ekle():
    print("Kitap eklendi!")

def kitap_sil():
    print("Kitap silindi!")

def kitap_goster():
    print("Tüm kitaplar listelendi!")

# Menü oluştur
menu = Menu("Kütüphane Menüsü")
menu.ekle("Kitap Ekle", kitap_ekle)
menu.ekle("Kitap Sil", kitap_sil)
menu.ekle("Kitapları Göster", kitap_goster)

# Çalıştır
menu.calistir()
