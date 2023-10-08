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
    hiding = input("where do you want to hid: ")
    print ("you will be hiding in", hiding)
    if hiding == "spot1":
        user1.user1HidingSpot1()
    else:
        user1.user1HidingSpot2()

if player == "user2":
    hiding = input("where do you want to hid: ")
    print (player, "you will be hiding in", hiding)
    if hiding == "spot1":
        user2.user2HidingSpot1()
    else:
        user2.user2HidingSpot2()

print ("the seeker will now chose if he will be going to spot 1 or spot 2 good luck")

