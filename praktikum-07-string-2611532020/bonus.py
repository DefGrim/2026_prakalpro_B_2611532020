# Name: Defran Naufalanski
# NIM: 2611532020
# Question Bonus

# "Kasur in rusak"
text = "Kasur ini rusak"

clean = text.lower().replace(" ", "")

if clean == clean[::-1]:
    result = "Palindrome"
else:
    result = "Not a palindrome"

print(result)

# "Algoritma"
text = "Algoritma"

clean = text.lower().replace(" ", "")

if clean == clean[::-1]:
    result = "Palindrome"
else:
    result = "Not a palindrome"

print(result)

# "Ada apa ada"
text = "Ada apa ada"

clean = text.lower().replace(" ", "")

if clean == clean[::-1]:
    result = "Palindrome"
else:
    result = "Not a palindrome"

print(result)