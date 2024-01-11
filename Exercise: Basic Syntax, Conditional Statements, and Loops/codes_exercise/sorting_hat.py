while True:
    names = input()
    
    if names == "Voldemort":
        print("You must not speak of that name!")
        break
    
    elif names == "Welcome!":
        print("Welcome to Hogwarts.")
        break

    lenght = len(names)

    if lenght < 5:
        print(f"{names} goes to Gryffindor.")
    elif lenght == 5:
        print(f"{names} goes to Slytherin.")
    elif lenght == 6:
        print(f"{names} goes to Ravenclaw.")
    elif lenght > 6:    # else:
        print(f"{names} goes to Hufflepuff.")
    
