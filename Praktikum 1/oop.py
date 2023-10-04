class BangunDatar:
    def __init__(self, panjang, lebar):
        self.panjang = panjang
        self.lebar = lebar

    def hitung_luas(self):
        return self.panjang * self.lebar

    def cetak_luas(self):
        print(f"Luas bangun datar adalah {self.hitung_luas()}")


class Persegi(BangunDatar):
    def __init__(self, sisi):
        super().__init__(sisi, sisi)


class PersegiPanjang(BangunDatar):
    def __init__(self, panjang, lebar):
        super().__init__(panjang, lebar)


class Segitiga(BangunDatar):
    def __init__(self, alas, tinggi):
        super().__init__(alas / 2, tinggi)


if __name__ == "__main__":
    # Input data dari user
    panjang = float(input("Masukkan panjang: "))
    lebar = float(input("Masukkan lebar: "))
    alas = float(input("Masukkan alas: "))
    tinggi = float(input("Masukkan tinggi: "))

    # Buat objek dari kelas BangunDatar
    persegi = Persegi(panjang)
    persegi_panjang = PersegiPanjang(panjang, lebar)
    segitiga = Segitiga(alas, tinggi)

    # Cetak luas bangun datar
    persegi.cetak_luas()
    persegi_panjang.cetak_luas()
    segitiga.cetak_luas()
