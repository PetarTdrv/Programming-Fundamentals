operator = input()
first_num = int(input())
second_num = int(input())

def calcultion(first_num, second_num, operator):
    if operator == "multiply":
        result = first_num * second_num
    elif operator == "divide":
        result = int(first_num / second_num)
    elif operator == "add":
        result = first_num + second_num
    elif operator == "subtract":
        result = first_num - second_num

    return result

print(calcultion(first_num, second_num, operator))
