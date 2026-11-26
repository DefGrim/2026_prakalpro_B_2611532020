class_list = input("Student numbers: ").split()
submitted_list = input("Submitted student numbers: ").split()

submitted_set = set(submitted_list)
not_submitted_set = set(class_list) - submitted_set

print(f"Submitted: {len(submitted_set)} students")
print(f"Not submitted: {len(not_submitted_set)} students")

for num in class_list:
    if num not in submitted_set:
        print(num)