import random

number_random_integers = 6
max_number = 45
min_number = 1
number_of_picks = int(input("How many quick picks? "))
for i in range(number_of_picks):
    numbers = []
    for j in range(number_random_integers):
        number = random.randint(min_number, max_number)
        while number in numbers:
            number = random.randint(min_number, max_number)
        numbers.append(number)
    numbers.sort()
    for number in numbers:
        print(f"{number:>2}", end=" ")
    print("\r")
