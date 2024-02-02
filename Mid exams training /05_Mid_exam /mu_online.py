start_healt = 100
start_bitcoins = 0
dunngeons_rooms = input().split("|")
best_room = 0
room_counter = 0
is_death = False

for room in dunngeons_rooms:
    
    room_parts = room.split()
    room_counter += 1
    best_room = room_counter

    if room_parts[0] == "potion":
        start_healt += int(room_parts[1])
        if start_healt < 100:
            print(f"You healed for {room_parts[1]} hp.")
            print(f"Current health: {start_healt} hp.")
        elif start_healt > 100:
            healt_calc = 100 - (start_healt - int(room_parts[1]))
            start_healt = 100
            print(f"You healed for {healt_calc} hp.")
            print(f"Current health: {start_healt} hp.")
    elif room_parts[0] == "chest":      
        start_bitcoins += int(room_parts[1])
        print(f"You found {int(room_parts[1])} bitcoins.")
    else:
        if start_healt > 0:
            monster = room_parts[0]
            start_healt -= int(room_parts[1])
            if start_healt > 0:
                print(f"You slayed {monster}.")
            else:
                is_death = True
                
    if is_death == True:
        print(f"You died! Killed by {monster}.")
        print(f"Best room: {best_room}")
        exit()

print("You've made it!")
print(f"Bitcoins: {start_bitcoins}")
print(f"Health: {start_healt}")
