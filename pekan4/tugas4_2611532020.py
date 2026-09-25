print("=== SISTEM LOKET ALPRO ADVENTURE PARK ===")

nama_pengunjung_2020 = input("Masukkan Nama Pengunjung        : ").strip()
umur_2020 = int(input("Input umur anda                 : "))

print(f"Nama Pengunjung : {nama_pengunjung_2020}")
print(f"Umur            : {umur_2020} tahun")

sim_2020 = input("Apakah Anda Sudah Punya SIM C (y/t): ").strip().lower()
if sim_2020:
    sim_2020 = sim_2020[0]

print()
print("Pilihan Paket Wahana (1-5):")
print("  1. Safari Rimba         (Rp 50,000)")
print("  2. Arung Jeram          (Rp 75,000)")
print("  3. Motor ATV Ekstrim    (Rp 120,000)")
print("  4. Roller Coaster Kilat (Rp 100,000)")
print("  5. All-Access VIP       (Rp 220,000)")

paket_pilihan_2020 = int(input("Masukkan nomor paket (1-5)      : "))
jumlah_tiket_2020 = int(input("Masukkan jumlah tiket           : "))

if jumlah_tiket_2020 <= 0:
    print("Kuota tiket tidak valid.")
    raise SystemExit

is_member_2020 = input("Apakah Anda member? (y/t)       : ").strip().lower()
if is_member_2020:
    is_member_2020 = is_member_2020[0]

kode_promo_valid_2020 = input("Apakah kode promo valid? (y/t)  : ").strip().lower()
if kode_promo_valid_2020:
    kode_promo_valid_2020 = kode_promo_valid_2020[0]

match paket_pilihan_2020:
    case 1:
        nama_paket_2020 = "Wahana Safari Rimba"
        harga_satuan_2020 = 50000
    case 2:
        nama_paket_2020 = "Wahana Arung Jeram"
        harga_satuan_2020 = 75000
    case 3:
        nama_paket_2020 = "Wahana Motor ATV Ekstrim"
        harga_satuan_2020 = 120000
    case 4:
        nama_paket_2020 = "Wahana Roller Coaster Kilat"
        harga_satuan_2020 = 100000
    case 5:
        nama_paket_2020 = "Wahana All-Access VIP"
        harga_satuan_2020 = 220000
    case _:
        print("Paket wahana tidak valid!")
        raise SystemExit

print()
print("--- KELAYAKAN PENGENDARA WAHANA ---")

if paket_pilihan_2020 == 3:
    if umur_2020 >= 17 and sim_2020 == 'y':
        print("Status Akses: Anda sudah dewasa dan boleh mengendarai ATV sendiri.")
    elif umur_2020 >= 17 and sim_2020 != 'y':
        print("Status Akses: Anda sudah dewasa tetapi tidak boleh bawa motor ATV (wajib didampingi instruktur).")
    elif umur_2020 < 17 and sim_2020 == 'y':
        print("Status Akses: Identitas tidak valid: Belum cukup umur memiliki SIM.")
    else:
        print("Status Akses: Anda belum cukup umur dan tidak boleh bawa motor ATV.")
else:
    if umur_2020 >= 10:
        print("Status Akses: Anda memenuhi syarat usia untuk wahana ini.")
    else:
        print("Status Akses: Anda belum cukup umur untuk wahana ini.")

subtotal_2020 = harga_satuan_2020 * jumlah_tiket_2020
total_diskon_persen_2020 = 0

if subtotal_2020 >= 200000:
    total_diskon_persen_2020 += 10
if is_member_2020 in ['y', 'ya']:
    total_diskon_persen_2020 += 5
if kode_promo_valid_2020 in ['y', 'ya']:
    total_diskon_persen_2020 += 15
if jumlah_tiket_2020 >= 5:
    total_diskon_persen_2020 += 5

nominal_diskon_2020 = subtotal_2020 * (total_diskon_persen_2020 / 100)
total_bayar_2020 = subtotal_2020 - nominal_diskon_2020

print()
print("--- Rincian Pembayaran ---")
print(f"Subtotal Belanja : Rp {subtotal_2020:,.0f}")
print(f"Total Diskon     : {total_diskon_persen_2020}% (Rp {nominal_diskon_2020:,.0f})")
print(f"Total Bayar      : Rp {total_bayar_2020:,.0f}")

print("Catatan Layanan  : ", end="")
if total_bayar_2020 > 300000:
    print("Selamat! Anda berhak mendapatkan Souvenir Gratis.")
else:
    print("Terima kasih telah berkunjung.")

print("Program Selesai")
