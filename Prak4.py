class PersegiPanjang:
    
    def __init__(self, panjang, lebar):
        self.panjang = panjang
        self.lebar = lebar
    def keliling(self):
        return 2 * (self.panjang + self.lebar)
    def luas(self):
        return self.panjang * self.lebar
    def __str__(self):
        return f"persegi panjang, panjang {self.panjang} cm, dan lebar {self.lebar} cm"

if __name__ == "__main__":
    
    pp = PersegiPanjang(3, 2)
    print(pp)
    print("Luas:", pp.luas(), "cm²")
    print("Keliling:", pp.keliling(), "cm")

#jadi "def" yang pertama itu kontruktor pertama untuk menginput class dari panjang dan lebar,
#lalu "def" yang kedua untuk menghitung keliling 
#nah di "def" yang ketiga untuk menghitung luas dari persegi panjang 
#dan "def" yang terakhir untuk menampilkan hasil dari panjang dan lebar dari peregi panjang 
#selanjutnya
#ada if __name__ == "__main__": itu untuk mengeksekusi program utama dari class persegi panjang
#dibawahnya diikuti variabel pp yang diisi dengan class persegi panjang dengan panjang 3 dan lebar 2
#lalu diikuti dengan print untuk menampilkan hasil dari class persegi panjang, luas, dan keliling
#Print pertama untuk menampilkan hasil dari class persegi panjang
#print kedua untuk menampilkan hasil dari luas persegi panjang
#print ketiga untuk menampilkan hasil dari keliling persegi panjang
#jika ingin menambahkan tinggi dari persegi panjang bisa dimulai dari "def __init__(self, panjang, lebar, tinggi)
#lalu diikuti dengan self.tinggi = tinggi
#dan di "def" yang terakhir untuk menampilkan hasil dari panjang, lebar, dan tinggi dari peregi panjang
#untuk printnya bisa ditambahkan print("Tinggi:", pp.tinggi, "cm")
#