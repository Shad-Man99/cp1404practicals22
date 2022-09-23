"""Password checker"""


def main():
    min_length = 10
    password = input("Enter password: ")
    get_password(min_length, password)


def get_password(min_length, password):
    while len(password) < min_length:
        print("Invalid password, please choose a longer password")
        password = input("Enter password: ")
    else:
        print_password(password)


def print_password(password):
    print("*" * len(password))


main()
