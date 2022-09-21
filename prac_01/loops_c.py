# "c. print n stars. Ask the user for a number, then print that many stars (*), all on one line.
# Note: this is a very simple loop for repeating n times. We use for loops for "definite" iteration like this.
# while loops are used for "indefinite" iteration (like repeating while a user input is incorrect).
# Sample output:
#
# Number of stars: 4
# **** "

number = int(input("Enter number: "))
print("Number of stars:", number)
for i in range(number):
    print("*", end="")


