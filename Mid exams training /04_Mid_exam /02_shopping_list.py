l = input().split("!")
product_list = l

while True:
    command = input().split()

    if command[0] == "Go" and command[1] == "Shopping!":
        break

    if command [0] == "Urgent":
        if command[1] in product_list:
            continue
        else:
            product_list.insert(0, command[1])
    
    elif command[0] == "Unnecessary":
        if command[1] in product_list:
            product_list.remove(command[1])
    
    elif command[0] == "Correct":
        if command[1] in product_list:
            index = product_list.index(command[1])
            del product_list[index]
            product_list.insert(index, command[2])

    elif command[0] == "Rearrange":
        if command[1] in product_list:
            removed_item = command[1]
            product_list.remove(command[1])
            product_list.append(removed_item)


print(", ".join(product_list))
