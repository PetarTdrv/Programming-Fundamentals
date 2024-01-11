coffees_count = 0

while True:
    command = input()

    if command == "END":
        if coffees_count > 5:
            print("You need extra sleep")
            break
        else:
            print(coffees_count)
            break
    elif command == "coding" or command == "dog" or command == "cat" or command == "movie" \
        or command == "CODING" or command == "DOG" or command == "CAT" or command == "MOVIE":
        if command.islower():
            coffees_count += 1
        elif command.isupper():
            coffees_count += 2
    else:
        continue
