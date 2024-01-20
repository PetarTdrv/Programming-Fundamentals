string = input().split(" ")
number_list = list(map(int, string))
modified_list = []

for num in number_list:
    if num < 0:
        num = num * -1
        modified_list.append(num)
    elif num > 0:
        num = num * -1
        modified_list.append(num)
    else:
        modified_list.append(num)

print(modified_list) 
