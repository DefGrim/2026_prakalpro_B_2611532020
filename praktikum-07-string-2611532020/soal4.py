# Name: Defran Naufalanski
# NIM: 2611532020
# Question 4

# Bagian A
phone = "08123456789"
masked = phone[:4] + "*" * 4 + phone[-4:]
print(masked)


# Bagian B-C
# Tabel no-1
phone = "081234567890"
hidden = len(phone) - 7
masked = phone[:4] + "*" * hidden + phone[-3:]
print(masked)

# Tabel no-2
phone = "08123456789"
hidden = len(phone) - 7
masked = phone[:4] + "*" * hidden + phone[-3:]
print(masked)

# Tabel no-3
phone = "0812345678"
hidden = len(phone) - 7
masked = phone[:4] + "*" * hidden + phone[-3:]
print(masked)

# Tabel no-4 (NIM)
phone = "082611532020"
hidden = len(phone) - 7
masked = phone[:4] + "*" * hidden + phone[-3:]
print(masked)