#slow but small
import random

def user2hiding():
    diceroll = random.randint(2,12)
    if diceroll == 2 or diceroll == 3 or diceroll == 4 or diceroll == 5:
        print("you died whit a dice roll of", diceroll, "game over")
        exit()
    else:
        print("you have survied step 1 whit a roll of", diceroll) 


def user2beingseeked():
    diceroll2 = random.randint(2,12)
    if diceroll2 == 2 or diceroll2 == 3:
       print("The seeker has found whit a roll of", diceroll2, "game over")
       exit()
    else:
        print("you have not yet ben found luck numer", diceroll2, "saved you")
