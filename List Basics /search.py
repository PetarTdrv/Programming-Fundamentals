lines = int(input())
word = input()

default_list = []
filtered_list = []

for i in range(lines):
    strings = input()
    default_list.append(strings)
    if word in strings:
        filtered_list.append(strings)

print(default_list)
print(filtered_list)
