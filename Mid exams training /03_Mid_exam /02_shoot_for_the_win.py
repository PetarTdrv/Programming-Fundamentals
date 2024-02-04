targets = list(map(int, input().split()))
shot_targets = 0
 
while True:
    command = input()
    if command == 'End':
        print(f"Shot targets: {shot_targets} -> {' '.join(map(str, targets))}")
        break
 
    index = int(command)
    if index in range(len(targets)):
        current_number = targets[index]
        for i in range(len(targets)):
            if targets[i] != -1:
                if targets[i] > current_number:
                    targets[i] -= current_number
                else:
                    targets[i] += current_number
        targets[index] = -1
        shot_targets += 1
