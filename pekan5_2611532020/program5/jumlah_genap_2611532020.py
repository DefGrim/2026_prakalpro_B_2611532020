# Buat file dengan nama jumlah_genap_NIM.py
# buat program untuk menghitung perulangan  for dalam Python
# Nama variable ditambah 4 digit nim terakhir contoh: ulang_1234
# Program ini menggunakan fungsi input()

ulang_2020 = int(input("Masukkan nilai batas: "))

jumlah_2020 = 0
for i_2020 in range(1, ulang_2020 + 1):
    if i_2020 % 2 == 0:
        print(i_2020, end=" ")
        jumlah_2020 = jumlah_2020 + i_2020

        if i_2020 < ulang_2020:
            print(" + ", end=" ")
        else:
            print(" = ", jumlah_2020, end=" ")
print()
print("Jumlah =", jumlah_2020)