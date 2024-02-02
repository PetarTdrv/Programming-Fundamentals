items = input().split(", ")
items_list = items

while True:
    command = input().split(" - ")

    if command[0] == "Craft!":
        break
    
    elif command[0] == "Collect":
        if command[1] in items_list:
            continue
        else:
            items_list.append(command[1])
    elif command[0] == "Drop":
        if command[1] in items_list:
            items_list.remove(command[1])
    elif command[0] == "Combine Items":
        new_items = command[1].split(":")
        if new_items[0] in items_list:
            find_index = items_list.index(new_items[0])
            items_list.insert(find_index + 1, new_items[1])
    elif command[0] == "Renew":
        if command[1] in items_list:
            find_index = items_list.index(command[1])
            change_position_of_element = items_list.pop(find_index)
            items_list.append(change_position_of_element)

message = ", ".join(items_list)
print(message)
