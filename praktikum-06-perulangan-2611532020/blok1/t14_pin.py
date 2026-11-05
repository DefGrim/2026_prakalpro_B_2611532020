MAX_ATTEMPTS = 3                 # H
correct_pin = "1234"             # K
attempt = 1                      # B
pin = input("Enter PIN: ")       # E
if pin == correct_pin:           # J
    print("Access granted")      # D
else:
    while pin != correct_pin and attempt < MAX_ATTEMPTS: # C
        print("Incorrect PIN.")  # I
        attempt += 1             # G
        pin = input("Enter PIN: ") # E
    else:                        # F
        print("Account locked")  # A