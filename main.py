"""
python giriş.pdf
1- B
2- E
3- C
4- B
5- B
6- C

1- C
2- C
3- B
4- ses çıkarırlar, miyav

sorular1.docx
1-  Arabalar sınıfında Toyota ve Corolla marka ve model bilgileriyle
    yeni bir nesne oluşturulmuş ve bilgileri_yazdir metoduyla bu 
    bilgiler ekrana yazılmış.

sorular2.docx
    ||
    ||
    ||
   \  /
    \/
"""

class Insan():
    def __init__(self, isim, yas):
        self.isim = isim
        self.yas = yas
    
    def konus(self):
        print("\nMerhaba, ben herhangi bir insanım. Adım " + str(self.isim) + ".")

class Hoca(Insan):
    def __init__(self, isim, yas, sicil_no):
        super().__init__(isim, yas)
        self.sicil_no = sicil_no
    
    def konus(self):
        print("\nMerhaba, ben bir öğretmenim. Adım " + str(self.isim) + ".")
    
    def ders_ver(self):
        print("\nBir öğretmenim ve ders veriyorum. Sicil numaram:" + str(self.sicil_no))

class Ogrenci(Insan):
    def __init__(self, isim, yas, sinif):
        super().__init__(isim, yas)
        self.sinif = sinif
    
    def konus(self):
        print("\nMerhaba, ben bir öğrenciyim. Adım " + str(self.isim) + ".")
    
    def kendini_tanit(self):
        print("\nBir öğrenciyim ve " + str(self.sinif) + ". sınıfa gidiyorum.")

class Sekreter(Insan):
    def __init__(self, isim, yas, sirket):
        super().__init__(isim, yas)
        self.sirket = sirket
    
    def konus(self):
        print("\nMerhaba, size nasıl yardımcı olabilirim? Adım " + str(self.isim) + ".")
    
    def sirketi_tanit(self):
        print("\nMerhaba, " + str(self.sirket) + " olarak saygılarımızı sunarız.")

Ahmet = Insan("Ahmet", 20)
Ayşe = Hoca("Ayşe", 30, 123345)
Burhan = Ogrenci("Burhan", 10, 6)
Berrin = Sekreter("Berrin", 20, "Abara Araç Kiralama")

Ahmet.konus()
Ayşe.konus()
Ayşe.ders_ver()
Burhan.konus()
Burhan.kendini_tanit()
Berrin.konus()
Berrin.sirketi_tanit()


