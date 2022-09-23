"""Test"""

min_length = 10
password = input("Enter password: ")
while len(password) < min_length:
    print("Invalid password length, enter a longer password")
    password = input("Enter password: ")
else:
    print("*" * len(password))
