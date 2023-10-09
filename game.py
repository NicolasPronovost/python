import random
import app
import user1
import user2

player=app.step1()
if player == "user1":
    user1.user1hiding()
else:
    user2.user2hiding()    

if player == "user1":
    hiding = input("You made it here whit out detection now you have a choise. spot1 is close but but dosn't provid lots of cover, spot2 is a little farther down the road but has a nice box to hid behind. Where are you going to hid?: ")
    print ("Bold of you let's hope it works out in", hiding)
    if hiding == "spot1":
        user1.user1HidingSpot1()
    else:
        user1.user1HidingSpot2()

if player == "user2":
    hiding = input("You made it here whit out detection now you have a choise. spot1 is close but but dosn't provid lots of cover, spot2 is a little farther down the road but has a nice box to hid behind. Where are you going to hid?: ")
    print (player, "That's a bold choise let's hope it workes out for you in", hiding)
    if hiding == "spot1":
        user2.user2HidingSpot1()
    else:
        user2.user2HidingSpot2()

print ("the seeker will now chose if he will be going to spot 1 or spot 2 good luck")

seeker = random.randint(1,2)
print ("the seeker is going to spot", seeker)


if seeker == 1:
    if hiding == "spot1":
        print("the seeker has chosent your hiding spot good luck")
        if player == "user1":
            print ("the seeker is at your hiding spot you chooses speed over size you got a slim chance he dosn't see you good luck")
            diceroll = random.randint(2,12)
            print ("you need a 12 or an 11 to survive let's see what you roll. You rolled", diceroll)
            if diceroll == 12 or diceroll == 11:
                print ("wow he didn't see you congradulations you have won the hardest way possible")
                exit()
            else:
                print ("the seeker saw you... You try to run but it's no use you look back and all you see is darknes death you just lost")
                exit()
        else:
            print ("you sacrifisted speed for this moment right here your small let's hope the seeker can't see you behind the box")
            diceroll = random.randint(2,12)
            print ("you need a 12 to a 9 to survive let's see what you roll. You rolled", diceroll)
            if diceroll == 12 or diceroll == 11 or diceroll == 10 or diceroll == 9:
                print ("I always knew it was going to work out for you. You have won the hardest way possible")
                exit()
            else:
                print ("the seeker saw you... You try to run but it's no use you look back and all you see is darknes death you just lost")
                exit()
    else:
        print ("the seeker did not come to your hiding spot congrats you win")
        exit()

if seeker == 2:
    if hiding == "spot2":
        print("the seeker has chosent your hiding spot good luck")
        if player == "user1":
            print ("the seeker is at your hiding spot you chooses speed over size you got a slim chance he dosn't see you good luck")
            diceroll = random.randint(2,12)
            print ("you need a 12 or an 11 to survive let's see what you roll. You rolled", diceroll)
            if diceroll == 12 or diceroll == 11:
                print ("wow he didn't see you congradulations you have won the hardest way possible")
                exit()
            else:
                print ("the seeker saw you... You try to run but it's no use you look back and all you see is darknes death you just lost")
                exit()
        else:
            print ("you sacrifisted speed for this moment right here your small let's hope the seeker can't see you behind the box")
            diceroll = random.randint(2,12)
            print ("you need a 12 to a 9 to survive let's see what you roll. You rolled", diceroll)
            if diceroll == 12 or diceroll == 11 or diceroll == 10 or diceroll == 9:
                print ("I always knew it was going to work out for you. You have won the hardest way possible")
                exit()
            else:
                print ("the seeker saw you... You try to run but it's no use you look back and all you see is darknes death you just lost")
                exit()
    else:
        print ("the seeker did not come to your hiding spot congrats you win")
        exit()