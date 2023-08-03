from random import randint

t = ["Rock", "Paper", "Scissors"]

computer = t[randint(0,2)]

you = False

while you == False:
    print("\nRock, Paper, Scissors ??")
    you = input("Enter Your Choice : ")

    if you == computer:
        print("\nTie!")
    elif you == "Rock":
        if computer == "Paper":
            print("\nComputer chose : " , computer)
            print("You chose : ", you)
            print(computer, "covers", you)
            print("You Lost this Round")
        else:
            print("\nComputer chose : " , computer)
            print("You chose : ", you)
            print(you, "breaks", computer)
            print("Hurrah !! You Won !!")

    elif you == "Paper":
        if computer == "Scissors":
            print("\nComputer chose : " , computer)
            print("You chose : ", you)
            print(computer, "cut", you)
            print("You Lost this Round")
        else:
            print("\nComputer chose : " , computer)
            print("You chose : ", you)
            print(you, "covers", computer)
            print("Hurrah !! You Won !!")

    elif you == "Scissors":
        if computer == "Rock":
            print("\nComputer chose : " , computer)
            print("You chose : ", you)
            print(computer, "breaks", you)
            print("You Lost this Round")
        else:
            print("\nComputer chose : " , computer)
            print("You chose : ", you)
            print(you, "cut", computer)
            print("Hurrah !! You Won !!")
    elif you == "Q":
        break
    else:
        print("\nTurn Invalid. Check your spelling!")

    you = False
    computer = t[randint(0,2)]

