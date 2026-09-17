# Buat file dengan nama perbandingan_NIM.py
# Nama variabel ditambah 4 digit nim terakhir contoh: angka1_1234
# Program ini menggunakan fungsi input()
# Nilai yang dimasukkan akan dikonversi menjadi tipe data integer
# Program operator perbandingan dalam Python

angka1_2020 = int(input("Input angka-1: "))
angka2_2020 = int(input("Input angka-2: "))

# Lebih besar dari
hasil = angka1_2020 > angka2_2020
print("\nOperator lebih besar dari")
print("angka1_2020 > angka2_2020 =", hasil)

# Lebih kecil dari
hasil = angka1_2020 < angka2_2020
print("\nOperator lebih kecil dari")
print("angka1_2020 < angka2_2020 =", hasil)

# Lebih besar dari atau sama dengan
hasil = angka1_2020 >= angka2_2020
print("\nOperator lebih besar dari atau sama dengan")
print("angka1_2020 >= angka2_2020 =", hasil)