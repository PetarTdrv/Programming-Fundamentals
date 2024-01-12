wd = input().lower()
equal_to_words = ["Sand", "Water", "Fish", "Sun"]
count = 0

for word in equal_to_words:
    count += wd.count(word.lower())

print(count)
