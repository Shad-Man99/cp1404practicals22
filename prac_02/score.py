""" Gets user score and calculates result, calculates result from random score"""
import random


def main():
    score = float(input("Enter score: "))
    while score != 0:
        result = calculate_result(score)
        print(result)
        score = float(input("Enter score: "))
    random_score = random.randint(0, 100)
    result = calculate_result(random_score)
    print(f"Random score was {random_score}, which is {result}.")


def calculate_result(score):
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    elif score < 50:
        return "Bad"


main()
