def even_numbers(numbers_as_digits):
    even_nums = []
    
    for number in numbers_as_digits:
        if number % 2 == 0:
            even_nums.append(number)

    return even_nums

numbers = input().split()
nums_as_digits = [int(num) for num in numbers]
print(even_numbers(nums_as_digits))
