# Buat file dengan nama assignment_NIM.py
# Nama variabel ditambah 4 digit nim terakhir contoh: angka1_1234
# Program ini menggunakan fungsi input()
# Nilai yang dimasukkan akan dikonversi menjadi tipe data integer
# Program operator assignment dalam Python

angka1_2020 = int(input("Input angka-1: "))
angka2_2020 = int(input("Input angka-2: "))

print("\nNilai awal angka1_2020 =", angka1_2020)
print("Nilai awal angka2_2020 =", angka2_2020)

# Assignment biasa
hasil = angka1_2020
print("\nAssignment Biasa (=)")
print("Hasil =", hasil)

# Assignment penambahan
hasil = angka1_2020
hasil += angka2_2020
print("\nAssignment penambahan (+=)")
print("Hasil =", hasil)

# Assignment pengurangan
hasil = angka1_2020
hasil -= angka2_2020
print("\nAssignment pengurangan (-=)")
print("Hasil =", hasil)

# Assignment perkalian
hasil = angka1_2020
hasil *= angka2_2020
print("\nAssignment perkalian (*=)")
print("Hasil =", hasil)

# Assignment pembagian, pembagian bulat, dan sisa bagi
if angka2_2020 != 0:
    hasil = angka1_2020
    hasil /= angka2_2020
    print("\nAssignment pembagian (/=)")
    print("Hasil =", hasil)
    # Operator tambahan
    hasil = angka1_2020
    hasil //= angka2_2020
    print("\nAssignment pembagian bulat (//=)")
    print("Hasil =", hasil)
    hasil = angka1_2020
    hasil %= angka2_2020
    print("\nAssignment sisa bagi (%=)")
    print("Hasil =", hasil)
else:
    print("\nPembagian tidak dapat dilakukan.")
    print("Angka kedua tidak boleh bernilai 0.")

# Operator tambahan: assigment perpangkatan
hasil = angka1_2020
hasil **= angka2_2020
print("\nAssignment perpangkatan (**=)")
print("Hasil =", hasil)