# Buat file dengan nama perbandingan_NIM.py
# Nama variabel ditambah 4 digit nim terakhir contoh: angka1_1234
# Program ini menggunakan fungsi input()
# Nilai yang dimasukkan akan dikonversi menjadi tipe data integer
# Program operator perbandingan dalam Python

angka1_2020 = int(input("Input angka-1: "))
angka2_2020 = int(input("Input angka-2: "))

# Lebih besar dari
hasil_2020 = angka1_2020 > angka2_2020
print("\nOperator lebih besar dari")
print("angka1_2020 > angka2_2020 =", hasil_2020)

# Lebih kecil dari
hasil_2020 = angka1_2020 < angka2_2020
print("\nOperator lebih kecil dari")
print("angka1_2020 < angka2_2020 =", hasil_2020)

# Lebih besar dari atau sama dengan
hasil_2020 = angka1_2020 >= angka2_2020
print("\nOperator lebih besar dari atau sama dengan")
print("angka1_2020 >= angka2_2020 =", hasil_2020) 

# Lebih kecil dari atau sama dengan
hasil_2020 = angka1_2020 <= angka2_2020
print("\nOperator lebih kecil dari atau sama dengan")
print("angka1_2020 <= angka2_2020 =", hasil_2020)

# Sama dengan
hasil_2020 = angka1_2020 == angka2_2020
print("\nOperator sama dengan")
print("angka1_2020 == angka2_2020 =", hasil_2020)

# Tidak sama dengan
hasil_2020 = angka1_2020 != angka2_2020
print("\nOperator tidak sama dengan")
print("angka1_2020 != angka2_2020 =", hasil_2020)

# Tambahan: perbandingan berantai dalam Python
hasil_2020 = 0 < angka1_2020 < 100
print("\nOperator perbandingan berantai")
print("0 < angka1_2020 < 100 =", hasil_2020)

hasil_2020 = 0 < angka2_2020 < 100
print("0 < angka2_2020 < 100 =", hasil_2020)