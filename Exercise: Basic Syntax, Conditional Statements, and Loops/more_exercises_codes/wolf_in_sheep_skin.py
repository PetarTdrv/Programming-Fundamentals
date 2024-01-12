text = input()

all_animals = text.split(", ")
position = len(all_animals) - 1

for animal in all_animals:
    if animal == "wolf" and position == 0:
        text = "Please go away and stop eating my sheep"
    elif animal == "wolf":
        text = f"Oi! Sheep number {position}! You are about to be eaten by a wolf!"

    position -= 1

print(text)
