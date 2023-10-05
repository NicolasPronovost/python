#fast but fat
import random

def user1hiding():
    diceroll = random.randint(2,12)
    if diceroll == 2 or diceroll == 3:
        print("you died whit a dice roll of", diceroll, "game over")
        exit()
    else:
        print("you have survied step 1 whit a roll of", diceroll)

def user1HidingSpot1():
    diceroll = random.randint(2,12)
    if diceroll == 2:
        print("you did not make it to the hiding spot in time. Your rolled a", diceroll, " and died game over")
        exit()
    else:
        print("You rolled a", diceroll, "and have made it to your hiding spot congrats")


def user1HidingSpot2():
    diceroll = random.randint(2,12)
    if diceroll == 2 or diceroll ==3:
        print("you did not make it to the hiding spot in time. Your rolled a", diceroll, " and died game over")
        exit()
    else:
        print("You rolled a", diceroll, "and have made it to your hiding spot congrats")

