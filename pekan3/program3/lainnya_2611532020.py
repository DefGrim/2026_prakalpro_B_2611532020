# Buat file dengan nama lainnya_NIM.py
# Nama variabel ditambah 4 digit nim terakhir contoh: angka1_1234
# Program ini menggunakan fungsi input()
# Program operator keanggotaan dan identitas

print("==================================")
print("1. OPERATOR KEANGGOTAAN")
print("==================================")

# Input beberapa data yang dipisahkan dengan koma
input_data = input("Masukkan beberapa data, pisahkan dengan koma: ")

# Mengubah input menjadi list integer
data = [int(angka.strip()) for angka in input_data.split(",")]

nilai_dicari = int(input("Masukkan nilai yang ingin dicari: "))

# Operator in
hasil = nilai_dicari in data
print("\nOperator keanggotaan IN")
print(nilai_dicari, "in", data, "=", hasil)

# Operator not in
hasil = nilai_dicari not in data
print("\nOperator keanggotaan NOT IN")
print(nilai_dicari, "not in", data, "=", hasil)


print("\n==================================")
print("2. OPERATOR IDENTITAS")
print("==================================")

# objek1 menggunakan list dari input pengguna
objek1_2020 = data

# objek2 menggunakan list dari input pengguna
objek2_2020 = objek1_2020

# objek3 memiliki isi yang sama, tatpi merupakan objek yang baru
objek3_2020 = data.copy()

print("objek1_2020:", objek1_2020)
print("objek2_2020:", objek2_2020)
print("objek3_2020:", objek3_2020)

# Operator is
hasil = objek1_2020 is objek2_2020
print("\nOperator identitas IS")
print("objek1_2020 is objek2_2020 =", hasil)

# Operator is not
hasil = objek1_2020 is not objek3_2020
print("\nOperator identitas IS NOT")
print("objek1_2020 is not objek3_2020 =", hasil)

# Membandingkan identitas dan nilai
print("\nPerbandingan identitas dan nilai")
print("objek1_2020 is objek3_2020 =", objek1_2020 is objek3_2020)
print("objek1_2020 == objek3_2020 =", objek1_2020 == objek3_2020)