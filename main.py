import random
def rock(choose, random):
    if(choose == "rock" and random == "rock"):
        print("The Game is draw")
    elif(choose == "rock" and random == "paper"):
        print("You Loose")
    elif(choose == "rock" and random == "scissors"):
        print("You Win")
def paper(choose, random):
    if(choose == "paper" and random == "rock"):
        print("You Win")
    elif(choose == "paper" and random == "paper"):
        print("The game is draw")
    elif(choose == "paper" and random == "scissors"):
        print("You Loose")
def scissors(choose, random):
    if(choose == "scissors" and random == "rock"):
        print("YOu Loose")
    elif(choose == "scissors" and random == "paper"):
        print("You Win")
    elif(choose == "scissors" and random == "scissors"):
        print("The game is draw")
    elif(choose != "rock" and "paper" and "scissors"):
        print("Choose correct option")
def exit(close):
    if(close == "yes"):
        quit()
    elif(close == "no"):
        print("Lets continue playing")
    else:
        print("Give me correct command to close the game")
def main():
    game = ["rock", "paper", "scissors"]
    randoms = random.choice(game)
    while True:
        user = input("Pick anyone of the opition(ROck/ Paper / Scissoors): ")
        print("The AI choose: ", randoms)
        rock(user, randoms)
        paper(user, randoms)
        scissors(user, randoms)
        print(" ")
        choice = input("Press YES/NO to quit: ")
        exit(choice)
        print(" ")

main()

