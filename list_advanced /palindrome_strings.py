words = input().split()
special_palindrome = input()
palindromes = []

for element in words:
    if element == element[::-1]:
        palindromes.append(element)

print(palindromes)
print(f"Found palindrome {palindromes.count(special_palindrome)} times")
