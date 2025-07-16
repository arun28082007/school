"""
#This code generates a random sequence of values from a predefined list and prints them in a specific format.
import random

val = [10,20,30,40,50,60,70,80]
begin = random.randint(1,3)
last  = random.randint(begin,7)

for i in range(100):
    for x in range(begin, last +1):
        print(val[x] , end='_')

"""

def 