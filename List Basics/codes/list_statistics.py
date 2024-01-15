n = int(input())

positive = []
negative = []

for _ in range(n):
    number = int(input())
    if number > 0:
        positive.append(number)
    elif number == 0:
        pass
    else:
        negative.append(number)

print(positive)
print(negative)

sum_of_negative = 0
for i in negative:
    sum_of_negative += i

print(f"Count of positives: {len(positive)}")
print(f"Sum of negatives: {sum_of_negative}")
