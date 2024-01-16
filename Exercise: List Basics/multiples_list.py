factor = int(input())
max_lenght = int(input())

multiplied_list = []
factor_sum = factor
multiplied_list.append(factor_sum)

for i in range(1, max_lenght):
    factor_sum += factor
    multiplied_list.append(factor_sum)

print(multiplied_list)
