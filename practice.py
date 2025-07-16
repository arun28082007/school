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

def changelist(m,n):
    m[0] = 25
    n[0] = [2,3]
l1 = [-11,21]
l2 = [14,23]
changelist(l1, l2)
print(l1[0], '#', l2[0])