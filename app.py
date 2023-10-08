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

def step2user1():
    print ("Have have survied step 1 now chose your hiding sport")
    choose = True
    while choose:
        hidingspot = input ("where are you going to hid?: ")
        if hidingspot == "user1HidingSpot1" or hidingspot == "user1HidingSpot2":
            print ("You will be hiding at", hidingspot, "good luck")
            choose = False
    return(hidingspot)

def seeker():
    diceroll = random.randint(1,2)
    if diceroll == 1:
       print("the seeker has chosen to go and investiagte spot 1")
    else:
        print("the seeker is going to investigate spot 2")