budget = int(input())

price = 0

while True:
    command = input()

    if command == "End":
        print("You bought everything needed.")
        break
    
    product_price = int(command)
    price += product_price

    if price > budget:
        print("You went in overdraft!")
        break
