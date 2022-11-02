import collections
import random

end_spot = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']

start = 4
chip = start
results = []
for y in range(100):
    for x in range(8):
        if chip == 0.5:
            chip += 0.5
        elif chip == 9.5:
            chip -= 0.5
        else:
            chip = chip + random.choice([-0.5, 0.5])
    results.append(chip)
print(results)

counter=collections.Counter(results)
print(counter)