def even_odd_sum(numbers_as_str):
    sum_of_even = []
    sum_of_odd = []
    
    for num in numbers_as_str:
        if int(num) % 2 == 0:
            sum_of_even.append(int(num))
        else:
            sum_of_odd.append(int(num))

    return f"Odd sum = {sum(sum_of_odd)}, Even sum = {sum(sum_of_even)}"

n = int(input())
numbers_as_string = []
for ns in str(n):
    numbers_as_string.append(ns)
print(even_odd_sum(numbers_as_string))
