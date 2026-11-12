# Name: Defran Naufalanski
# NIM: 2611532020
# Question 1

name = "Defran Naufalanski".lower()
nim = "2611532020"

clean = name.strip()
space = clean.find(" ")
if space == -1:
    first = clean
else:
    first = clean[:space]

username = first.lower() + nim[-3:]
intake_year = "20" + nim[:2]

print("=" * 30)
print("         STUDENT CARD         ")
print("=" * 30)
print(f"{'Name':<10} : {name.title()}")
print(f"{'NIM':<10} : {nim}")
print(f"{'Username':<10} : {username}")
print(f"{'Intake':<10} : {intake_year}")
print("=" * 30)