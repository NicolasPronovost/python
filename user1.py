#fast but big
import random

def user1hiding():
    diceroll = random.randint(2,12)
    if diceroll == 2 or diceroll == 3:
        print("you took your time walking over to the satrting point and it cost you. Whit a roll of", diceroll, "you didn't even make it and got cought, game over")
        exit()
    else:
        print("you have survied step 1 whit a roll of", diceroll)

def user1HidingSpot1():
    diceroll = random.randint(2,12)
    if diceroll == 2:
        print("you did not make it to the hiding spot in time. Your rolled a", diceroll, "and got cought game over")
        exit()
    else:
        print("You rolled a", diceroll, "and have made it to your hiding spot congrats")


def user1HidingSpot2():
    diceroll = random.randint(2,12)
    if diceroll == 2 or diceroll ==3:
        print("you did not make it to the hiding spot in time. Your rolled a", diceroll, "and got cought game over")
        exit()
    else:
        print("You rolled a", diceroll, "and have made it to your hiding spot congrats")

