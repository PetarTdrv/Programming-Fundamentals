def aritmetic_mean(numbers_as_digits):
    return (sum(numbers_as_digits) / len(numbers_as_digits))

number_of_digits = int(input())
numbers = []

for _ in range(number_of_digits):
    num = int(input())
    numbers.append(num)

print(f"\n{aritmetic_mean(numbers):.2f}")
