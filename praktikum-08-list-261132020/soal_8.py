number_of_rows = 4
seats_per_row = 5

# Buat denah 4 baris x 5 kursi ('.' = kosong), setiap baris objek list terpisah
seating = [["." for _ in range(seats_per_row)] for _ in range(number_of_rows)]

while True:
  for r_idx in range(number_of_rows):
    print(f"Row {r_idx + 1}: " + " ".join(seating[r_idx]))

  row_num = int(input("Row (0 to stop): "))
  if row_num == 0:
    break

  seat_num = int(input("Seat: "))

  if (
      row_num < 1
      or row_num > number_of_rows
      or seat_num < 1
      or seat_num > seats_per_row
  ):
    print("Invalid seat.")
  elif seating[row_num - 1][seat_num - 1] == "X":
    print("Seat already taken.")
  else:
    seating[row_num - 1][seat_num - 1] = "X"
    print("Seat booked.")

seats_taken = 0
for r_idx in range(number_of_rows):
  for c_idx in range(seats_per_row):
    if seating[r_idx][c_idx] == "X":
      seats_taken += 1

print(f"Seats taken: {seats_taken}")