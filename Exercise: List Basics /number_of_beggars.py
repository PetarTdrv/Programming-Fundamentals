money_as_string = input().split(", ")
number_of_beggars = int(input())
money_as_digits = []

for str in money_as_string:
    money_as_digits.append(int(str))

start_index = 0
step = number_of_beggars
final_sums = []

for i in range(number_of_beggars):
    sum = 0
    for current_index in range(start_index, len(money_as_digits), step):
        sum += money_as_digits[current_index]
    final_sums.append(sum)
    start_index += 1

print(final_sums)
