# Buat file dengan nama nested_for2_NIM.py
# Buat program untuk perulangan for dalam Python
# nama variable ditambah 4 digit nim terakhir contoh: ulang_1234
# Program ini menggunakan fungsi input()

batas_2020 = int(input("Masukkan nilai batas: "))
for i_2020 in range(1, batas_2020 + 1):
    for j_2020 in range(1, batas_2020 + 1):
        print("*", end="")
    print() # pindah ke baris berikutnya