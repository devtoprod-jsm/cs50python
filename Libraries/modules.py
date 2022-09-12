import random
from random import choice
import statistics

print(random.choice([0,1]))

def choice():
    print("Hello")

print(random.randint(-10,10))

cards = ["Jacks","Queens","Kings","Aces"]
random.shuffle(cards)
print(cards)

print(statistics.mean([1,2]))