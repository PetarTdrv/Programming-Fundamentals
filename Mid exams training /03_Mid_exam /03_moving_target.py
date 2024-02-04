sequence_of_targets = input().split(' ')
sequence_of_targets = [int(x) for x in sequence_of_targets]
command = input()
 
while command != 'End':
    command = command.split(' ')
    action = command[0]
    index = int(command[1])
 
    if action == 'Shoot':
        power = int(command[2])
        if index in range(len(sequence_of_targets)):
            if sequence_of_targets[index] - power > 0:
                sequence_of_targets[index] -= power
            else:
                sequence_of_targets.pop(index)
 
    elif action == 'Add':
        value = int(command[2])
        if index in range(len(sequence_of_targets)):
            sequence_of_targets.insert(index, value)
        else:
            print('Invalid placement!')
 
    elif action == 'Strike':
        radius = int(command[2])
        before_radius = index - radius
        after_radius = index + radius
 
        if after_radius in range(len(sequence_of_targets)):
            sequence_of_targets = sequence_of_targets[0:before_radius] + sequence_of_targets[after_radius + 1::]
        else:
            print('Strike missed!')
 
    command = input()
 
result = '|'.join(str(x) for x in sequence_of_targets)
print(result)
