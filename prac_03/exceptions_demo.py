"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
2. When will a ZeroDivisionError occur?
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    while denominator == 0:
        print("Cannot divide by 0")
        denominator = int(input("Enter the denominator: "))
    else:
        fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
print("Finished.")


# Q1. A ValueError will occur when a non-integer has been inputted. E.g. a special character
# Q2. A ZeroDivisionError will occur when the denominator is 0, as this is not mathematically possible.
# Q3. Yes, refer to code.

