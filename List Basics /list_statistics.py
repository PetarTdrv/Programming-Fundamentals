n = int(input())

negatives = []
positives = []

sum_of_negatives = 0
count_positives = 0

for i in range(n):
    number = int(input())

    if number > 0:
        positives.append(number)
    elif number < 0:
        negatives.append(number)
    else:
        continue

count_positives = len(positives)
sum_of_negatives = sum(negatives)

print(positives)
print(negatives)
print(f"Count of positives: {count_positives}")
print(f"Sum of negatives: {sum_of_negatives}")
