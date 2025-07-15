import random

'''This script generates 100 random integers between 1 and 10,
counts the frequency of each number, and prints the results.
It uses the `Counter` class from the `collections` module to tally the occurrences.

from collections import Counter

results = [random.randint(1, 10) for _ in range(100)]
frequency = Counter(results)

for number in range(1, 11):
    print(f"{number}: {frequency[number]}")
'''

'''
for i in range(4):
    #print(int(random.randint(1, 4  )))  # Generates 4 random floats between 1 and 4
    #print(int(100 + random.randint(1, 4)))  # Generates 4 random integers between 100 and 104
    #print(int(random.random() * 5 + 5))  # Generates 4 random integers between 5 and 9
'''

'''
for i in range(1000):
    print(int((random.random())*5)+100,end=' ')

# generate 1000 random integers between 100 and 104
'''


'''
city = ['delhi', 'mumbai', 'chennai', 'kolkata',]
pick = random.randint(0,3)
for i in city:
    for j in range(1, pick):
        print(i, end=' ')
    print()
# This code randomly selects a city from the list and prints it a number of times
# equal to the random number generated between 1 and 3.

'''


s = 0
L = [1, 2, "three", "four", 4,5]
for i in L:
    if isinstance(i, int):
        s += i
print(s)  # This will print the sum of integers in the list L





