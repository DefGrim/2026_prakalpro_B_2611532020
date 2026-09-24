print("=== SISTEM TRANSAKSI TOKO ===")

nama_2020 = input("Masukkan Nama Pelanggan : ")
status_2020 = input("Masukkan Status Pelanggan (member/nonmember) : ").lower()
total_belanja_2020 = float(input("Masukkan Total Belanja : Rp"))
jumlah_barang_2020 = int(input("Masukkan Jumlah Barang : "))
kode_promo_2020 = input("Masukkan Kode Promo : ").upper()

syarat_belanja_2020 = total_belanja_2020 >= 200000
syarat_barang_2020 = jumlah_barang_2020 >= 3
status_member_2020 = status_2020 == "member"

daftar_promo_2020 = ["HEMAT10", "HEMAT20", "GRATISONGKIR"]

promo_tersedia_2020 = kode_promo_2020 in daftar_promo_2020
promo_tidak_tersedia_2020 = kode_promo_2020 not in daftar_promo_2020

diskon_member_2020 = status_member_2020 and syarat_belanja_2020

promo_didapatkan_2020 = promo_tersedia_2020 and (syarat_belanja_2020 or syarat_barang_2020)

bukan_member_2020 = not status_member_2020

if diskon_member_2020:
    persentase_diskon_2020 = 0.10
else:
    persentase_diskon_2020 = 0.05 if syarat_belanja_2020 else 0

besar_diskon_2020 = total_belanja_2020 * persentase_diskon_2020

total_pembayaran_2020 = total_belanja_2020 - besar_diskon_2020

if jumlah_barang_2020 > 0:
    rata_rata_barang_2020 = total_belanja_2020 / jumlah_barang_2020
else:
    rata_rata_barang_2020 = 0

sisa_pembagian_2020 = int(total_belanja_2020) % jumlah_barang_2020 if jumlah_barang_2020 > 0 else 0


poin_2020 = 0
if status_member_2020:
    poin_2020 += int(total_pembayaran_2020 // 10000)

jumlah_barang_tersisa_2020 = jumlah_barang_2020
if promo_didapatkan_2020:
    jumlah_barang_tersisa_2020 -= 1

kode_1_2020 = ["HEMAT10"]
kode_2_2020 = ["HEMAT10"]

nilai_sama_2020 = kode_1_2020 == kode_2_2020
objek_sama_2020 = kode_1_2020 is kode_2_2020
objek_berbeda_2020 = kode_1_2020 is not kode_2_2020


kode_member_2020 = 1 if status_member_2020 else 0
kode_belanja_2020 = 2 if syarat_belanja_2020 else 0
kode_barang_2020 = 4 if syarat_barang_2020 else 0
kode_promo_2020 = 8 if promo_tersedia_2020 else 0

# Operator OR (|)
kode_status_2020 = (
    kode_member_2020
    | kode_belanja_2020
    | kode_barang_2020
    | kode_promo_2020
)

cek_member_2020 = kode_status_2020 & 1
cek_belanja_2020 = kode_status_2020 & 2
cek_barang_2020 = kode_status_2020 & 4
cek_promo_2020 = kode_status_2020 & 8

kode_referensi_2020 = 11
perbandingan_status_2020 = kode_status_2020 ^ kode_referensi_2020

kode_shift_2020 = kode_status_2020 << 1


member_access_2020 = bool(cek_member_2020)
promo_access_2020 = bool(cek_promo_2020)
free_shipping_access_2020 = syarat_belanja_2020 and syarat_barang_2020


print("\n=== DATA PELANGGAN ===")
print("Nama Pelanggan       :", nama_2020)
print("Status Pelanggan     :", status_2020)
print("Total Belanja        : Rp", total_belanja_2020)
print("Jumlah Barang        :", jumlah_barang_2020)
print("Kode Promo           :", kode_promo_2020)


print("\n=== HASIL VALIDASI ===")
print("Belanja >= Rp200000  :", syarat_belanja_2020)
print("Jumlah Barang >= 3   :", syarat_barang_2020)
print("Status Member        :", status_member_2020)
print("Kode Promo Tersedia  :", promo_tersedia_2020)
print("Mendapatkan Diskon   :", diskon_member_2020)
print("Mendapatkan Promo    :", promo_didapatkan_2020) 


print("\n=== HASIL PERHITUNGAN ===")
print("Besarnya Diskon      : Rp", besar_diskon_2020)
print("Total Pembayaran     : Rp", total_pembayaran_2020)
print("Rata-rata Harga      : Rp", rata_rata_barang_2020)
print("Sisa Pembagian       :", sisa_pembagian_2020)


print("\n=== HAK AKSES PELANGGAN ===")
print("Kode Hak Akses       :", format(kode_status_2020, "04b"))
print("Member Access        :", member_access_2020)
print("Promo Access         :", promo_access_2020)
print("Free Shipping Access :", free_shipping_access_2020)
print("Poin Pelanggan       :", poin_2020)


print("\n=== OPERATOR IDENTITAS ===")
print("kode_1 == kode_2     :", nilai_sama_2020)
print("kode_1 is kode_2     :", objek_sama_2020)
print("kode_1 is not kode_2 :", objek_berbeda_2020)


print("\n=== OPERASI BITWISE ===")
print("=== Kode Status Transaksi ===")
print("0001 | 0010 | 0100 | 1000")

print("Kode Biner           :", format(kode_status_2020, "04b"))
print("Kode Desimal         :", kode_status_2020)

print("\n=== PEMERIKSAAN STATUS ===")

print("\nCek Member")
print(format(kode_status_2020, "04b"), "& 0001")
print("Hasil Biner         :", format(cek_member_2020, "04b"))
print("Hasil Desimal       :", cek_member_2020)

print("\nCek Belanja")
print(format(kode_status_2020, "04b"), "& 0010")
print("Hasil Biner         :", format(cek_belanja_2020, "04b"))
print("Hasil Desimal       :", cek_belanja_2020)

print("\nCek Jumlah Barang")
print(format(kode_status_2020, "04b"), "& 0100")
print("Hasil Biner         :", format(cek_barang_2020, "04b"))
print("Hasil Desimal       :", cek_barang_2020)

print("\nCek Promo")
print(format(kode_status_2020, "04b"), "& 1000")
print("Hasil Biner         :", format(cek_promo_2020, "04b"))
print("Hasil Desimal       :", cek_promo_2020)

print("\n=== PERBANDINGAN STATUS (XOR) ===")
print("Kode Transaksi      :", format(kode_status_2020, "04b"))
print("Kode Referensi      :", format(kode_referensi_2020, "04b"))
print(format(kode_status_2020, "04b"), "^",
      format(kode_referensi_2020, "04b"))
print("Hasil Biner         :", format(perbandingan_status_2020, "04b"))
print("Hasil Desimal       :", perbandingan_status_2020)

print("\n=== SHIFT ===")
print(format(kode_status_2020, "04b"), "<< 1")
print("Hasil Biner         :", format(kode_shift_2020, "b"))
print("Hasil Desimal       :", kode_shift_2020)

print("\n=== SELESAI ===")