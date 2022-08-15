# This program emulates a dice roll
import random

def roll(output):
    output = random.randrange(1, 7)
    return output

start = input("Enter r to roll the dice\n")
while start == "r":
    result = 0
    print(roll(result), '\n ----------------------------------------------------------------')
    start = input("Enter r to continue rolling or enter anything else to quit\n")

