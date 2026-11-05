total = 0

while True:
    number = int(input("Enter a number: "))
    
    if number < 0:
        break
    elif number == 0:
        continue
    
    print(f"Positive number: {number}")
    total += number

print(f"Total: {total}")