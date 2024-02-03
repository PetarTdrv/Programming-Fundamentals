nums_as_string = input().split()
nums_as_digits = [int(num) for num in nums_as_string]
average_sum = sum(nums_as_digits) / len(nums_as_digits)
l_nums = []

for digit in nums_as_digits:
    if digit > average_sum:
        l_nums.append(digit)
        l_nums.sort()
        l_nums.reverse()

if len(l_nums) == 0:
    print("No")

l_nums = l_nums[:5]

l_str = [str(n) for n in l_nums]

message = " ".join(l_str)
print(message)
