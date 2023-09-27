import random

def rollDice(modifier):
    return random.randrange(2,11) + modifier

print (rollDice(2))
