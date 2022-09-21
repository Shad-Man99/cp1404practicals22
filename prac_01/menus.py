MENU = """H - (H)ello
G - (G)oodbye
Q - (Q)uit"""
name = input("Enter name: ").upper()
print(MENU)
choice = input(">>> ").upper()
while choice != "Q":
    if choice == "H":
        print("(H)ello", name)
    elif choice == "G":
        print("(G)oodbye", name)
    else:
        print("Invalid option")
    print(MENU)
    choice = input(">>> ").upper()
print("Thank you.")
