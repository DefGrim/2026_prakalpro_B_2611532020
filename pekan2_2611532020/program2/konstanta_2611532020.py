# Buat file dengan nama Konstanta_NIM.py
# Program in menggunakan konstanta untuk menghitung luas lingkaran
# Nama variabel ditambah 4 digit nim terakhir contoh: jari_2020

from typing import Final
PI: Final = 3.14
print("pi: %f" % (PI))
jari_2020 = float(input("Masukkan nilai jari-jari: "))
luas_2020 = PI * jari_2020 * jari_2020
print("Luas lingkaran dengan jari-jari %.2f adalah %.2f" % (jari_2020, luas_2020))