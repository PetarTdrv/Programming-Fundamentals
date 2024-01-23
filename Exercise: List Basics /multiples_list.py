factor = int(input())
count = int(input())
max_sz = count * factor
list = []
for i in range(factor, max_sz + 1, factor):
    list.append(i)
print(list)
