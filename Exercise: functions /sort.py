def sort(list):
    return sorted(list)


numbers_as_string = input().split()
numbers_as_digits = [int(num) for num in numbers_as_string]
print(sort(numbers_as_digits))
