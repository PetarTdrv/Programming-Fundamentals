import random

rock = "Rock"
paper = "Paper"
scissors = "Scissors"

player_move = input("Choose [r]ock, [p]aper or [s]cissors: ").lower()

if player_move == "r":
    player_move = rock
elif player_move == "p":
    player_move = paper
elif player_move == "s":
    player_move = scissors
else:
    exit("Invalid Input. Try again...")

computer_random_number = random.randint(1, 3)

computer_move = ""

while True:
    if computer_random_number == 1:
        computer_move = rock
    elif computer_random_number == 2:
        computer_move = paper
    elif computer_random_number == 3:
        computer_move = scissors

    if (player_move == rock and computer_move == scissors) or \
            (player_move == paper and computer_move == rock) or \
            (player_move == scissors and computer_move == paper):
        print(f"The computer choose {computer_move}")
        print("You win!")
    elif (player_move == scissors and computer_move == rock) or \
            (player_move == rock and computer_move == paper)or\
            (player_move == paper and player_move == scissors):
        print(f"The computer choose {computer_move}")
        print("You lose!")
    else:
        print(f"The computer choose {computer_move}")
        print("Draw!")

    cont = input("Type [yes] to Play Agan or [no] to quit: ").lower()

    if cont == "yes":
        continue
    else:
        print("Thank you for playing!")
        break
