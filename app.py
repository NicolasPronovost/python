import random
import user1
import user2

def step1():
    print ("Welcom to hide or die.")
    choose = True
    while choose:
        print ("You have 2 options for who you would like to play as. Mark aka user1 he is fast on his feat but on the larger size. He will get to where he wants to go fast but good luck missing him.")
        print ("Next is David aka user2. He won't be seeting the world record in the 100m but he is samll, like really small. If you get to where you want to go the seeker will have a hard time seeing you.")
        player = input ("So who are you going to chose. user1 or user2: ")
        if player == "user1" or player == "user2":
            print("That's a bold chose. Let's see how it works out whit", player)
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