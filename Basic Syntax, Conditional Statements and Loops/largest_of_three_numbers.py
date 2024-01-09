first_number = int(input())
second_number = int(input())
third_number = int(input())

if first_number > second_number and first_number > third_number:
    print(first_number)
elif second_number > first_number and second_number > third_number:
    print(second_number)
elif third_number > second_number and third_number > first_number:
    print(third_number)
