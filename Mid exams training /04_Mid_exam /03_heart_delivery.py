neighborhood = [int(n) for n in input().split('@')]
 
command = input()
jump_length = 0
while not command == 'Love!':
    jump, index = command.split()
    index = int(index)
    jump_length += index
 
    if len(neighborhood) > jump_length:
        if neighborhood[jump_length] <= 0:
            print(f"Place {jump_length} already had Valentine's day.")
        else:
            neighborhood[jump_length] -= 2
            if neighborhood[jump_length] <= 0:
                print(f"Place {jump_length} has Valentine's day.")
    else:
        jump_length = 0
        if neighborhood[jump_length] <= 0:
            print(f"Place {jump_length} already had Valentine's day.")
        else:
            neighborhood[jump_length] -= 2
            if neighborhood[jump_length] <= 0:
                print(f"Place {jump_length} has Valentine's day.")
    command = input()
 
counter = 0
for n in neighborhood:
    if n > 0:
        counter += 1
 
print(f"Cupid's last position was {jump_length}.")
if not counter == 0:
    print(f"Cupid has failed {counter} places.")
else:
    print("Mission was successful.")
