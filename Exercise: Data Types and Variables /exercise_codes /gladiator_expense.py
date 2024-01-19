lost_fights = float(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

total_broken_helmet = lost_fights // 2
total_broken_swords = lost_fights // 3
total_shield_broken = lost_fights // (2*3)
total_armor_broken = total_shield_broken // 2

expenses = (total_broken_helmet * helmet_price) + (total_broken_swords * sword_price) + (total_shield_broken * shield_price) + (total_armor_broken * armor_price)

print(f"Gladiator expenses: {expenses:.2f} aureus")
