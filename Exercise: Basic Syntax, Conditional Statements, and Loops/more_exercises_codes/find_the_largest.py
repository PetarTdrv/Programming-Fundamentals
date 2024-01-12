num = int(input())
number = str(num)
nums = []

for i in number:
    nums.append(i)
    numbers = [int(x) for x in nums]
    sorted_list = sorted(numbers)

reversed_sorted_list = list(reversed(sorted_list))

for num in reversed_sorted_list:
    print(num, end="")
