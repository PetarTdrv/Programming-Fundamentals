number_of_wagons = int(input())
l_of_w = ["0"] * number_of_wagons
list_of_wagons = [int(string) for string in l_of_w]

while True:
    command = input().split()

    if command[0] == "End":  # After end print(list_fo_wagons)
        print(list_of_wagons)
        break

    elif command[0] == "add":
        list_of_wagons[-1] += int(command[1])

    elif command[0] == "insert":
        list_of_wagons[int(command[1])] += int(command[2])

    elif command[0] == "leave":
        list_of_wagons[int(command[1])] -= int(command[2])
