class Menu:
    def __init__(self, baslik):
        self.baslik = baslik
        self.ogeler = []

    def ekle(self, ad, fonksiyon):
        """Menüye yeni bir öğe ekler."""
        self.ogeler.append((ad, fonksiyon))

    def goster(self):
        """Menü başlığını ve öğeleri ekrana yazdırır."""
        print(f"\n=== {self.baslik} ===")
        for i, (ad, _) in enumerate(self.ogeler, start=1):
            print(f"{i}. {ad}")
        print(f"{len(self.ogeler) + 1}. Çıkış")

    def calistir(self):
        """Menüyü kullanıcıyla etkileşime sokar."""
        while True:
            self.goster()
            try:
                secim = int(input("\nBir seçenek seçiniz: "))
                if secim == len(self.ogeler) + 1:
                    print("Programdan çıkılıyor...")
                    break
                elif 1 <= secim <= len(self.ogeler):
                    _, fonksiyon = self.ogeler[secim - 1]
                    fonksiyon()
                else:
                    print("Geçersiz seçim, tekrar deneyin.")
            except ValueError:
                print("Lütfen sayısal bir değer girin.")
