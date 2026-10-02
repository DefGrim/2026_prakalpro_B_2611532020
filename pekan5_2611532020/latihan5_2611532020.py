#  Buatlah program untuk menampilkan tinggi segitiga menggunakan perulangan for

tinggi_2020 = int(input("Masukkan tinggi segitiga: "))

for i_2020 in range(1, tinggi_2020 + 1):
    print(" " * (tinggi_2020 - i_2020), end="")
    
    for j_2020 in range(i_2020):
        if j_2020 < (i_2020 - 1):
            print("*", end=" ")
    
    print()