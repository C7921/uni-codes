# Rock, Paper Scissors - Version 2
import random 
import time


moves = ["rock", "paper", "scissors"]

def player1():
    p1Move=None
    while (p1Move not in moves):
        p1Move=input("Enter your move Player 1! ").lower()
        if (p1Move not in moves):
            print("Sorry, that's not a valid move!")
        else:
            print("Player 1 entered", p1Move)
            return(p1Move)

def player2():
    p2Move=None
    while (p2Move not in moves):
        p2Move=input("Enter your move Player 2! ").lower()
        if (p2Move not in moves):
            print("Sorry, that's not a valid move!")
        else:
            print("Player 2 entered", p2Move)
            return(p2Move)

def computerMove():
    return(random.choice(moves))

def displayResult(winner):
    print(f"And the winner is...\n{winner}!")

def findWinner(p1, p2):
    if (p1 == p2):
        winner="it's a draw"
    elif (p1 == "rock") and (p2 == "scissors") or (p1 == "scissors") and (p2 == "paper") or (p1 == "paper") and (p2 == "rock"):
        winner = "Player 1"
    else:
        winner = "Player 2"
    return(winner)


print("Rock... \nPaper... \nScissors...")
opponent = None
while (opponent != "0"):
    opponent = input(
        "Are you playing against a human? (H/C) or 0 to Quit: ").lower()
    if (opponent[0] == "h"):
        print("Playing against a human.")
        p1=player1()
        p2=player2()
        displayResult(findWinner(p1, p2))
    elif (opponent[0] == "c"):
        print("Playing against Computer.")
        p1=player1
        cpuMove=computerMove()
        displayResult(findWinner(p1, cpuMove))
    elif (opponent[0] == "0"):
        print("Thanks for playing!")
    else:
        print("Sorry, that isn't valid!")
