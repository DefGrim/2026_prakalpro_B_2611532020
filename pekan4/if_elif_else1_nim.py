# Buat file dengan nama if_elif_else1_nim.py
# Buat program untuk kondisional if
# Nama variabel ditambah 4 digit nim terakhir contoh: ipk_1234
# Program ini menggunakan fungsi input ()

umur_2020 = int(input("Input umur anda: "))
sim_2020 = input("Apakah Anda Sudah Punya Sim C: ")[0]

if umur_2020 >= 17 and sim_2020 == 'y':
    print("Anda Sudah Dewasa dan boleh bawa motor")
elif umur_2020 >= 17 and sim_2020 != 'y':
    print("Anda Sudah Dewasa tetapi tidak boleh bawa motor")
elif umur_2020 < 17 and sim_2020 == 'y':
        print("Anda Belum Cukup Umur punya SIM")
else:
    print("Anda Belum Cukup Umur dan Tidak boleh bawa motor")
print("Program Selesai")