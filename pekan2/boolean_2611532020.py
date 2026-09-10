# Buat file dengan nama Boolean_NIM.py
# Nama variabel ditambah 4 digit nim terakhir contoh: nilai_1234
# Deklarasi variabel dengan tipe data Boolean
is_lulus = True
is_cumlaude = True

# Menggunakan Boolean
nilai_2020 = 85
batas_lulus_2020 = 75

# Menentukan nilai Booelean dari kondisi
status_kelulusan_2020 = nilai_2020 >= batas_lulus_2020 # Hasilnya akan True

print("=== Check Kelulusan ===")
print("Nilai:", nilai_2020)
print("Apakah lulus?", status_kelulusan_2020)
if is_lulus and is_cumlaude:
    print("Selamat! Anda lulus dengan predikat Cum Laude!")