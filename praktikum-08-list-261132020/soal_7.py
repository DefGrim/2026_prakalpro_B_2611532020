menus = ["Nasi Goreng", "Mie Ayam", "Soto"]
number_of_days = 3
sales = []

# Baca data dengan nested loop; setiap baris dibuat sebagai list baru lalu di-append() ke sales
for day_idx in range(number_of_days):
  row = []
  for menu_idx in range(len(menus)):
    val = int(input(f"Day {day_idx + 1}, {menus[menu_idx]}: "))
    row.append(val)
  sales.append(row)

# Cetak total porsi setiap hari (traversal per baris)
print("Total per day:")
for day_idx in range(number_of_days):
  day_total = 0
  for menu_idx in range(len(menus)):
    day_total += sales[day_idx][menu_idx]
  print(f"Day {day_idx + 1}: {day_total}")

# Hitung total setiap menu (traversal per kolom), simpan sebagai list of tuple menu_totals
menu_totals = []
for menu_idx in range(len(menus)):
  col_total = 0
  for day_idx in range(number_of_days):
    col_total += sales[day_idx][menu_idx]
  menu_totals.append((menus[menu_idx], col_total))

print(f"Total per menu: {menu_totals}")

# Cari menu terlaris; jika sama, pilih yang muncul lebih dulu (pakai '>' agar tidak tertimpa saat sama)
best_name, best_total = menu_totals[0]
for name, total in menu_totals:
  if total > best_total:
    best_total = total
    best_name = name

print(f"Best seller: {best_name} ({best_total})")