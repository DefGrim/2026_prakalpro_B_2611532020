# Name: Defran Naufalanski
# NIM: 2611532020
# Question 1

text = "  belajar python di kampus  "
clean = text.strip()
print(len(text), len(clean))
print(clean.find("python"))
print(clean.find("java"))
print(clean.find("a"))
print(clean.replace("kampus", "rumah"))
print(clean.title())
print("py" in clean)
print("Py" in clean)