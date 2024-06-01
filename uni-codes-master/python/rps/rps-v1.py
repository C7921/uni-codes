# Rock Paper Scissors - Version 1 
import random
moves = ["rock", "paper", "scissors"]


def player1():
    p1Move=input("Enter your move P1! ").lower()
    return(p1Move)


def player2():
    p2Move = input("Enter your move P2! ").lower()
    return(p2Move)


def humanOpp():
    p1=player1()
    print("** Don't cheat **\n" * 20)
    p2=player2()
    return(p1, p2)


def computerOpp():
    p1=player1()
    cpuMove=random.choice(moves)
    print("The computer chose...", cpuMove)
    # return(cpuMove=random.choice(moves))
    return(p1, cpuMove)


def displayResult(winner):
    print(f"And the winner is...\n{winner}!")


def findWinner(p1, p2):
    if (p1 == p2):
        winner="it's a draw"
    elif (p1 == "rock") and (p2 == "scissors") or (p1 == "scissors") and (p2 == "paper") or (p1 == "paper") and (p2 == "rock"):
        winner="Player 1"
    elif (p2 == "rock") and (p1 == "scissors") or (p2 == "scissors") and (p1 == "paper") or (p2 == "paper") and (p1 == "rock"):
        winner="Player 2"
    return(winner)


print("Rock... \nPaper... \nScissors...")
opponent = None
while (opponent != "0"):
    opponent = input("Are you playing against a human? (H/C) or 0 to Quit: ").lower()
    if (opponent[0] == "h"):
        print("Playing against a human.")
        p1, p2=humanOpp()
        displayResult(findWinner(p1, p2))
    elif (opponent[0] == "c"):
        print("Playing against Computer.")
        p1, cpuMove=computerOpp()
        displayResult(findWinner(p1, cpuMove))
    elif (opponent[0] == "0"):
        print("Thanks for playing!")
    else:
        print("Sorry, that isn't valid!")
