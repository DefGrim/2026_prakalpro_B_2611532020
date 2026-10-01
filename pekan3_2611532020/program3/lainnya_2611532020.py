# Buat file dengan nama lainnya_NIM.py
# Nama variabel ditambah 4 digit nim terakhir contoh: angka1_1234
# Program ini menggunakan fungsi input()
# Program operator keanggotaan dan identitas

print("==================================")
print("1. OPERATOR KEANGGOTAAN")
print("==================================")

# Input beberapa data yang dipisahkan dengan koma
input_data_2020 = input("Masukkan beberapa data, pisahkan dengan koma: ")

# Mengubah input menjadi list integer
data_2020 = [int(angka.strip()) for angka in input_data_2020.split(",")]

nilai_dicari_2020 = int(input("Masukkan nilai yang ingin dicari: "))

# Operator in
hasil_2020 = nilai_dicari_2020 in data_2020
print("\nOperator keanggotaan IN")
print(nilai_dicari_2020, "in", data_2020, "=", hasil_2020)

# Operator not in
hasil = nilai_dicari_2020 not in data_2020
print("\nOperator keanggotaan NOT IN")
print(nilai_dicari_2020, "not in", data_2020, "=", hasil_2020)


print("\n==================================")
print("2. OPERATOR IDENTITAS")
print("==================================")

# objek1 menggunakan list dari input pengguna
objek1_2020 = data_2020

# objek2 menggunakan list dari input pengguna
objek2_2020 = objek1_2020

# objek3 memiliki isi yang sama, tatpi merupakan objek yang baru
objek3_2020 = data_2020.copy()

print("objek1_2020:", objek1_2020)
print("objek2_2020:", objek2_2020)
print("objek3_2020:", objek3_2020)

# Operator is
hasil_2020 = objek1_2020 is objek2_2020
print("\nOperator identitas IS")
print("objek1_2020 is objek2_2020 =", hasil_2020)

# Operator is not
hasil_2020 = objek1_2020 is not objek3_2020
print("\nOperator identitas IS NOT")
print("objek1_2020 is not objek3_2020 =", hasil_2020)

# Membandingkan identitas dan nilai
print("\nPerbandingan identitas dan nilai")
print("objek1_2020 is objek3_2020 =", objek1_2020 is objek3_2020)
print("objek1_2020 == objek3_2020 =", objek1_2020 == objek3_2020)