# # Fungsi untuk penambahan
# def luas(a, b):
#     return a + b

# # Fungsi untuk pengurangan
# def kurang(a, b):
#     return a - b

# # Fungsi untuk perkalian
# def kali(a, b):
#     return a * b

# # Fungsi untuk pembagian
# def bagi(a, b):
#     if b == 0:
#         return "Error: Pembagian oleh nol!"
#     return a / b

# modifikasi ke bangun datar
# Fungsi untuk menghitung luas
def luas(alas, tinggi):
    return 0.5 * alas * tinggi

# Fungsi untuk menghitung keliling


def keliling(sisiA, sisiB, sisiC):
    return sisiA + sisiB + sisiC


# # Menampilkan menu operasi
# print("Pilih operasi:")
# print("1. Penambahan")
# print("2. Pengurangan")
# print("3. Perkalian")
# print("4. Pembagian")
# Menampilkan menu operasi
print("Pilih operasi:")
print("1. Luas")
print("2. Keliling")


# Meminta pengguna untuk memasukkan pilihan
pilihan = input("Masukkan pilihan (1/2/3/4): ")

# Meminta pengguna untuk memasukkan dua angka


# Melakukan operasi sesuai pilihan pengguna
# if pilihan == '1':
#     print("Hasil penambahan:", luas(angka1, angka2))
# elif pilihan == '2':
#     print("Hasil pengurangan:", kurang(angka1, angka2))
# elif pilihan == '3':
#     print("Hasil perkalian:", kali(angka1, angka2))
# elif pilihan == '4':
#     print("Hasil pembagian:", bagi(angka1, angka2))
# else:
#     print("Pilihan tidak valid")

if pilihan == '1':
    angka1 = float(input("Masukkan alas: "))
    angka2 = float(input("Masukkan tinggi: "))
    print("Luas:", luas(angka1, angka2))
elif pilihan == '2':
    angka1 = float(input("Masukkan sisi a: "))
    angka2 = float(input("Masukkan sisi b: "))
    angka3 = float(input("Masukkan sisi c: "))
    print("Keliling:", keliling(angka1, angka2, angka3))
else:
    print("Pilihan tidak valid")
