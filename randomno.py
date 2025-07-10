import random
from collections import Counter

results = [random.randint(1, 100) for _ in range(1000)]
frequency = Counter(results)

for number in range(1, 101):
    print(f"{number}: {frequency[number]}")