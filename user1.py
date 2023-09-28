#fast but fat
import random

def user1hiding():
    diceroll = random.randint(2,12)
    if diceroll == 2 or diceroll == 3:
        print("you died whit a dice roll of", diceroll, "game over")
        exit()
    else:
        print("you have survied step 1 whit a roll of", diceroll)


