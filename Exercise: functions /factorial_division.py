from math import factorial

def fact_division(first, second):
    first_factorial = factorial(first)
    second_factorial = factorial(second)
    return f"{(first_factorial / second_factorial):.2f}"


first_number = int(input())
second_number = int(input())
print(fact_division(first_number, second_number))
