# Name: Defran Naufalanski
# NIM: 2611532020

# Question 6

# Pemanasan
first_name = " muhammad"
last_name = "rafi "
full_name = first_name.strip() + " " + last_name.strip()
print(full_name)
print(full_name.title())

# Masalah

# Siti
full_name = "  Siti Aisyah  "
nim = "2610511023"

clean = full_name.strip()
space = clean.find(" ")
if space == -1:
    first = clean
else:
    first = clean[:space]

username = first.lower() + nim[-3:]
print(username)

# Muhammad Rafi
full_name = "  Muhammad Rafi Pratama  "
nim = "2610511045"

clean = full_name.strip()
space = clean.find(" ")
if space == -1:
    first = clean
else:
    first = clean[:space]

username = first.lower() + nim[-3:]
print(username)

# Kartika
full_name = "  Kartika  "
nim = "2610511007"

clean = full_name.strip()
space = clean.find(" ")
if space == -1:
    first = clean
else:
    first = clean[:space]

username = first.lower() + nim[-3:]
print(username)

# Defran
full_name = "  Defran Naufalanski  "
nim = "2611532020"

clean = full_name.strip()
space = clean.find(" ")
if space == -1:
    first = clean
else:
    first = clean[:space]

username = first.lower() + nim[-3:]
print(username)

# Kartika, langsung memakai clean[:space] tanpa memeriksa nilai -1
full_name = "  Kartika  "
nim = "2610511007"

clean = full_name.strip()
space = clean.find(" ")
if space == -1:
    first = clean[:space]
else:
    first = clean[:space]

username = first.lower() + nim[-3:]
print(username)