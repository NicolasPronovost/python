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
    choose = True
    while choose:
        hidingspot = input("Where do you want to hid: ")
        if hidingspot == "spot1" or hidingspot == "spot2":
            print("you will be hiding at", hidingspot)
            choose = False
    return(player)

   

