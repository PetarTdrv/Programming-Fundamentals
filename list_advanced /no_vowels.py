word = input()
word_without_vowels = [letter for letter in word if letter.lower() not in ['a', 'o', 'u', 'e', 'i']]
print("".join(word_without_vowels))
