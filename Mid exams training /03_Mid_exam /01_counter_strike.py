start_energy = int(input())
energy = start_energy
message = ""
won_count = 0
 
while True:
    command = input()
 
    if command == "End of battle":
        message = f"Won battles: {won_count}. Energy left: {energy}"
        break
 
    energy_to_down = int(command)
 
    if energy - energy_to_down >= 0:
        won_count += 1
        energy -= energy_to_down
        if won_count % 3 == 0:
            energy += won_count
    else:
        message = f"Not enough energy! Game ends with {won_count} won battles and {energy} energy"
        break
 
print(message)
