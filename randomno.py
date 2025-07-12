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

for i in range(4):
    #print(int(random.randint(1, 4  )))  # Generates 4 random floats between 1 and 4
    #print(int(100 + random.randint(1, 4)))  # Generates 4 random integers between 100 and 104
    print(int(random.random() * 5 + 5))  # Generates 4 random integers between 5 and 9


