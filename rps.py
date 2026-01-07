from random import randint
t = ["Rock", "Paper", "Scissors"]
computer = t[randint(0,2)]
player = False
while not player:
    player = input("Rock,Paper,Scissors?")
    if player == computer:
        print("Idiot it's a tie")
    elif player == "Paper":
        if computer == "Scissors":
            print ("HAHA", computer, "cuts", player)
        else:
            print("Nice", player, "covers", computer)
    elif player == "Scissors":
        if computer == "Paper":
            print ("Nice", player, "cuts", computer)
        else:
            print("HAHA", computer, "smashes", player)
    elif player == "Rock":
        if computer == "Scissors":
            print("Nice", player, "smashes", computer)
        else:
            print("HAHA", computer, "covers", player)
    else:
        print("Check your spelling idiot")
player = False
computer = t[randint(0,2)]

