# Buat file dengan nama perulangan_for3_NIM.py
# Buat program untuk perulangan for dalam Python
# nama variable ditambah 4 digit nim terakhir contoh: ulang_1234
# Program ini menggunakan fungsi input()

ulang_2020 = int(input("Masukkan jumlah perulangan: "))

jumlah_2020 = 0
for i in range(1, ulang_2020 + 1):
    print(i, end=" ")
    jumlah_2020 = jumlah_2020 + i

    if i < ulang_2020:
        print(" + ", end=" ")
    else:
        print(" = ", jumlah_2020, end=" ")
print()
print("Jumlah =", jumlah_2020)