first_text = input()
second_text = input()

for i in range(len(first_text)):
     if first_text[i] != second_text[i]:
         first_text = second_text[:i + 1] + first_text[i + 1:]
         print(first_text)
