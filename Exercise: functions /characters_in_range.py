def char_between(first, second):
    character_list = []
    for char in range(ord(first) + 1, ord(second)):
        character_list.append(chr(char))
    message = " ".join(character_list)
    return message

first_char = input()
second_char = input()
print(char_between(first_char, second_char))
