number_of_lines = int(input())
capacity = 255
added_liters = 0

for i in range(number_of_lines):
    liters = int(input())
    added_liters += liters
    if added_liters > capacity:
        print("Insufficient capacity!")

print(added_liters)
