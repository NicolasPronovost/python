import random
import app
import user1
import user2

player=app.step1()
if player == "user1":
    user1.user1hiding()
else:
    user2.user2hiding()    

hidingspot=app.step2()
if hidingspot == "spot1":
    user1.user1HidingSpot1
else:
    user1.user1HidingSpot2

