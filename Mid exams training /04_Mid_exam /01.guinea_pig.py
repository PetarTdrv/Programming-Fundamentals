food_in_kilograms = float(input())
hay_in_kilograms = float(input())
cover_in_kilograms = float(input())
puppy_weight = float(input())

grams_food = food_in_kilograms * 1000
grams_hay = hay_in_kilograms * 1000
grams_cover = cover_in_kilograms * 1000
puppy_weight_in_grams = puppy_weight * 1000

quantitty_for_cover = 1/3 * puppy_weight_in_grams

for day in range(1, 31):
    
    grams_food -= 300

    if day % 2 == 0:
        grams_hay -= 0.05 * grams_food
    
    if day % 3 == 0:
        grams_cover -= quantitty_for_cover

    if grams_cover <= 0 or grams_food <= 0 or grams_hay <= 0:
        print("Merry must go to the pet store!")
        exit()
    

food_in_kilograms = grams_food / 1000
hay_in_kilograms = grams_hay / 1000
cover_in_kilograms = grams_cover / 1000

print(f"Everything is fine! Puppy is happy! Food: {food_in_kilograms:.2f}, Hay: {hay_in_kilograms:.2f}, Cover: {cover_in_kilograms:.2f}.")
