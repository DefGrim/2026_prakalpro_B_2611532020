# Buat file dengan nama nested_for4_NIM.py
# Buat program untuk perulangan for dalam Python
# nama variable ditambah 4 digit nim terakhir contoh: ulang_1234
# Program ini menggunakan fungsi input()

tinggi_2020 = int(input("Masukkan tinggi pola (bilangan genap, misal 10): "))

if tinggi_2020 % 2 != 0:
    print("Tinggi harus bilangan genap!")
else:
    a_2020 = tinggi_2020
    c_2020 = a_2020
    lebar_2020 = (2 * tinggi_2020) - 2
    
    for i_2020 in range(1, tinggi_2020 + 1):
        b_2020 = c_2020 + 1
        
        for j_2020 in range(1, lebar_2020 + 1):
            
            # Baris atas dan bawah
            if i_2020 == 1 or i_2020 == tinggi_2020:
                if j_2020 == 1 or j_2020 == lebar_2020:
                    print("#", end="")
                else:
                    print("=", end="")
            
            # Baris isi
            else:
                if j_2020 == 1 or j_2020 == lebar_2020:
                    print("|", end="")
                else:
                    if j_2020 == c_2020:
                        print("<", end="")
                    elif j_2020 == b_2020:
                        print(">", end="")
                    elif j_2020 == (lebar_2020 - c_2020):
                        print("<", end="")
                    elif j_2020 == (lebar_2020 - c_2020 + 1):
                        print(">", end="")
                    elif j_2020 > b_2020 and j_2020 < (lebar_2020 - c_2020):
                        print(".", end="")
                    else:
                        print(" ", end="")
                        
        print()
        
        # Logika asli Java
        a_2020 -= 1
        
        if a_2020 <= 0:
            c_2020 = (-a_2020) + 2
        else:
            c_2020 = a_2020