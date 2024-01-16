string = input().split(" ")

number_list = list(map(int, string))

modified_list = []

for num in number_list:
    if num < 0:
        pos = num * -1
        modified_list.append(pos)
    elif num > 0:
        neg = num * -1
        modified_list.append(neg)
    else:
        modified_list.append(num)

print(modified_list)
