from typing import Final
BATAS_LULUS: Final = 75.0

print("=== SISTEM REGISTRASI PRAKTIKAN ALPRO 2026 ===")
nama_2020 = input("Masukkan Nama: ")
jenis_kelamin_2020 = input("Masukkan Jenis Kelamin (L/P): ")
umur_2020 = int(input("Masukkan Umur: "))
skor_2020 = float(input("Masukkan Skor Tes Awal: "))
print("        ")
print("=== DATA PRAKTIKAN & HASIL PEMERIKSAAN ===")
alamat_2020 = """
Kos Airi,
Kec.Pauh,
Kota Padang"""
print("Nama Mahasiswa:", nama_2020, "| Tipe:", type(nama_2020))
print("Jenis Kelamin:", jenis_kelamin_2020, "| Tipe:", type(jenis_kelamin_2020))
print("Alamat Domisili: ", alamat_2020, "| Tipe:", type(alamat_2020))
print("Umur:", umur_2020, "| Tipe:", type(umur_2020))
print("Skor Tes Awal:", skor_2020, "| Tipe:", type(skor_2020))
token_2020 = 100+3j
print("ID Token Sinyal:", token_2020, "| Tipe:", type(token_2020))
print("        ")
print("=== STATUS KELULUSAN PRAKTIKUM ===")
print("Batas Minimum Nilai:", BATAS_LULUS, "| Tipe:", type(BATAS_LULUS))
print("Apakah Lulus?:", skor_2020 >= BATAS_LULUS, "| Tipe:", type(skor_2020 >= BATAS_LULUS))