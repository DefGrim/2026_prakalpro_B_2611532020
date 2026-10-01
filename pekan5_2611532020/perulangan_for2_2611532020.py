# Buat file dengan nama perulangan_for2_NIM.py
# Buat program untuk perulangan for dalam Python
# nama variable ditambah 4 digit nim terakhir contoh: ulang_1234
# Program ini menggunakan fungsi input()

ulang_2020 = int(input("Masukkan jumlah perulangan: "))
print("Perulangan ke-0 sampai ke-", ulang_2020-1)
for i in range(ulang_2020):
    print(i, end=" ")
print()
print("Perulangan ke-1 sampai ke-", ulang_2020)
for i in range(1, ulang_2020+1):
    print(i, end=" ")