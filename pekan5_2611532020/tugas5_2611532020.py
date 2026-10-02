print("=== PROGRAM JAM PASIR KRISTAL PALINDROMIK (PEKAN 5) ===")

ukuran_2020 = int(input("Masukkan ukuran skala jam pasir (N): "))

for bagian_2020 in range(2):
	if bagian_2020 == 0:
		print("#", end="")
	else:
		for garis_2020 in range(4 * ukuran_2020 + 5):
			print("=", end="")
		print("#")

for baris_2020 in range(2 * ukuran_2020 + 1):
	if baris_2020 <= ukuran_2020:
		tingkat_2020 = ukuran_2020 - baris_2020
	else:
		tingkat_2020 = baris_2020 - ukuran_2020

	print("|", end="")

	for spasi_2020 in range(1 + 2 * (ukuran_2020 - tingkat_2020)):
		print(" ", end="")

	for angka_2020 in range(tingkat_2020, 0, -1):
		print(angka_2020, end="")
		if angka_2020 > 1:
			print(" ", end="")

	if tingkat_2020 > 0:
		print(" ", end="")
	print("<*>", end="")
	if tingkat_2020 > 0:
		print(" ", end="")

	for angka_2020 in range(1, tingkat_2020 + 1):
		print(angka_2020, end="")
		if angka_2020 < tingkat_2020:
			print(" ", end="")

	for spasi_2020 in range(1 + 2 * (ukuran_2020 - tingkat_2020)):
		print(" ", end="")

	print("|")

for bagian_2020 in range(2):
	if bagian_2020 == 0:
		print("#", end="")
	else:
		for garis_2020 in range(4 * ukuran_2020 + 5):
			print("=", end="")
		print("#")
