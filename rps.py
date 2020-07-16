from random import randint

play = ["Rock", "Paper", "Scissor"]

computer = play[randint(0,2)]
player = False

while True:
    player = input("")

    if player == computer:
        print("You Tie")

    elif player == "Rock":
        if computer == "Paper":
            print("You Lose")
        else:
            print("You Win")

    elif player == "Paper":
        if computer == "Scissor":
            print("You Lose")
        else:
            print("You Win")

    elif player == "Scissor":
        if computer == "Rock":
            print("You Lose")
        else:
            print("You Win")


    computer = play[randint(0, 2)]















