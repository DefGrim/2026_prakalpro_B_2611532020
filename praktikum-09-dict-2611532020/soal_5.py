n = int(input("Enter number of deposits: "))
cash = {}

for _ in range(n):
    parts = input().split()
    name = parts[0]
    amount = int(parts[1])
    cash[name] = cash.get(name, 0) + amount

for name, total in cash.items():
    print(f"{name}: {total}")

total_cash = sum(cash.values())
print(f"Total cash: {total_cash}")

top_name = ""
top_amount = -1
for name, total in cash.items():
    if total > top_amount:
        top_amount = total
        top_name = name

print(f"Top contributor: {top_name} ({top_amount})")