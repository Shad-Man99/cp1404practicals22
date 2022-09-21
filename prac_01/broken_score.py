score = float(input("Enter score: "))
while score != 0:
    if score < 0 or score > 100:
        print("Invalid score")
    elif score >= 90:
        print("Excellent")
    elif score >= 50:
        print("Passable")
    elif score < 50:
        print ("Bad")
    score = float(input("Enter score: "))