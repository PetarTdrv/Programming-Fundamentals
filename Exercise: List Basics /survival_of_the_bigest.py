list_of_strings = input().split()
numbers_to_remove = int(input())
list_of_integers = []

for num in list_of_strings:
    list_of_integers.append(int(num))

for i in range(numbers_to_remove):
    list_of_integers.remove(min(list_of_integers))

print(", ".join(map(str, list_of_integers)))
