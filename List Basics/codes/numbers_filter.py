n = int(input())

numbers = []
filtered = []

for _ in range(n):
    number = int(input())
    numbers.append(number)

command = input()
if command == "even":
    for i in numbers:
        if i % 2 == 0:
            filtered.append(i)
elif command == "odd":
    for i in numbers:
        if i % 2 != 0:
            filtered.append(i)
elif command == "negative":
    for i in numbers:
        if i < 0:
            filtered.append(i)
elif command == "positive":
    for i in numbers:
        if i >= 0:
            filtered.append(i)

print(filtered)
