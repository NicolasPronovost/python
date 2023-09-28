import random
import user1
import user2

def step1():
    print ("This is hide or die")

    choose = True
    while choose:
        player = input("Who do you want to play as: ")
        if player == "user1" or player == "user2":
            print("you will be playing as", player)
            choose = False
    return(player)

def step2():
    userlocation = input("where would you like to hid: ")

