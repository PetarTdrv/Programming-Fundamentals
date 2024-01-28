def min_max_sum(digit_list):
    return f"The minimum number is {min(digit_list)}\nThe maximum number is {max(digit_list)}\nThe sum number is: {sum(digit_list)}"


numbers_as_str = input().split()
numbers_as_digit = [int(num) for num in numbers_as_str]
print(min_max_sum(numbers_as_digit))
