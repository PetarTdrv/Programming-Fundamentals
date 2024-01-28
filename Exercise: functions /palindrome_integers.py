numbers = input().split(", ")

for num in numbers:
    reversed_num = num[::-1]
    if reversed_num == num:
        print("True")
    else:
        print("False")
