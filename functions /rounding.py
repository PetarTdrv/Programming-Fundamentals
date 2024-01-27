numbers_as_string = input().split()
numbers = [float(string) for string in numbers_as_string]
rounded_numbers = []

for num in numbers:
    rounded_numbers.append(round(num))

print(rounded_numbers)
