loot = input().split('|')
sum_items = 0
 
while True:
    command = input().split()
    if command[0] == 'Yohoho!':
        break
 
    elif command[0] == 'Loot':
        for i in range(len(command)):
            if i == 0:
                continue
            item = command[i]
            if item not in loot:
                loot.insert(0, item)
 
    elif command[0] == 'Drop':
        idx = int(command[1])
        if 0 <= idx < len(loot):
            x = loot.pop(idx)
            loot.append(x)
        else:
            continue
 
    elif command[0] == 'Steal':
        n = int(command[1])
        if n >= len(loot):
            removed = loot
            print(', '.join(removed))
            print('Failed treasure hunt.')
            exit()
        else:
            removed = loot[-n:]
            del loot[-n:]
            print(', '.join(removed))
 
if len(loot) > 0:
    for i in range(len(loot)):
        sum_items += len(loot[i])
 
    avg = f'{sum_items / len(loot):.2f}'
    print(f'Average treasure gain: {avg} pirate credits.')
