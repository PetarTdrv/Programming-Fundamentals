n = int(input())
word = input()

all_string_list = []

for _ in range(n):
    some_string = input()
    all_string_list.append(some_string)
print(all_string_list)

for i in range(len(all_string_list) -1, -1, -1):
    element = all_string_list[i]
    if word not in element:
        all_string_list.remove(element)
print(all_string_list)
