word = input()

list = []

for index, letter in enumerate(word):
    if letter.isupper():
        list.append(index)

print(list)
