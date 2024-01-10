divider = int(input())
max = int(input())

max_number = 0

for number in range(1, max + 1):
    number_check = number / divider
    if 0 < number <= max and number_check.is_integer():
        max_number = number
print(max_number)
