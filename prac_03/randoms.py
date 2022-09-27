import random

print(random.randint(5, 20))  # line 1
print(random.randrange(3, 10, 2))  # line 2
print(random.uniform(2.5, 5.5))  # line 3

# Q1. 5 and 20. Random integers printed between 5 and 20, inclusive.
# Q2. 3 and 19. No, because the starting point is 3 and steps in intervals of 2, hence only 3,5,7,9 will be outputted.
# Q3. 2.5 and 5.5.

print(random.randint(0, 100))
