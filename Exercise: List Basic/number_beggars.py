sums_as_string = input().split(", ")
number_of_beggars = int(input())
sum_as_digits = []
final_list = []
start_index = 0

for element in sums_as_string:
    sum_as_digits.append(int(element))

while start_index < number_of_beggars:
    final_sum = 0
    for num in range(start_index, len(sum_as_digits), number_of_beggars):
        final_sum += sum_as_digits[num]
    final_list.append(final_sum)
    start_index += 1

print(final_list)
