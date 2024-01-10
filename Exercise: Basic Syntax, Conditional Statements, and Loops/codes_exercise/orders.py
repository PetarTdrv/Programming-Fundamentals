n = int(input())
total_price = 0


for i in range(n):
    price_for_cofee = 0
    price_for_capsule = float(input())
    days = int(input())
    needed_capsules_per_day = int(input())

    if 0.01 <= price_for_capsule <= 100.00 and 1 <= days <= 31 and 1 <=  needed_capsules_per_day <= 2000:
        price_for_cofee = price_for_capsule * days * needed_capsules_per_day
        total_price += price_for_cofee
        print(f"The price for the coffee is: ${price_for_cofee:.2f}")

print(f"Total: ${total_price:.2f}")
