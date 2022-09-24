MENU = """G - Get valid score
R - Print result
S-  Print stars
Q - Quit"""


def main():
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "G":
            score = get_valid_score()
        elif choice == "R":
            result = calculate_result(score)
            print(result)
        elif choice == "S":
            print("*" * score)
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()


def calculate_result(score):
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    elif score < 50:
        return "Bad"


def get_valid_score():
    score = int(input("Enter score: "))
    while score < 0 or score > 100:
        print("Invalid score.")
        score = int(input("Enter score: "))
    return score


main()