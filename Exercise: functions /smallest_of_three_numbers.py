def smallest_number(list_with_digits):
    return min(list_with_digits)


numbers_as_num = []
for i in range(3):
    number_as_string = int(input())
    numbers_as_num.append(number_as_string)

print(smallest_number(numbers_as_num))
