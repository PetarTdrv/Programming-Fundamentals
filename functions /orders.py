product = input()
quantity = int(input())

def value(product, quantity):
    if product == "coffee":
        result = f'{(1.50 * quantity):.2f}'
    elif product == "water":
        result = f'{(1.00 * quantity):.2f}'
    elif product == "coke":
        result = f'{(1.40 * quantity):.2f}'
    elif product == "snacks":
        result = f'{(2.00 * quantity):.2f}'

    return result

print(value(product, quantity))
