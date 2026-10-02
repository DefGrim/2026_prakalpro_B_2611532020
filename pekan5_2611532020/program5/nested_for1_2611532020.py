# Buat file dengan nama nested_for1_NIM.py
# Buat program untuk perulangan for dalam Python
# nama variable ditambah 4 digit nim terakhir contoh: ulang_1234
# Program ini menggunakan fungsi input()

batas_2020 = int(input("Masukkan nilai batas: "))
for line_2020 in range(1, batas_2020 + 1):
    for j_2020 in range(1, (-1 * line_2020 + batas_2020 + 1)):
        print(".", end="")
    print(line_2020)