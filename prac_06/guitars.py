"""
Estimate: 45 minutes
Actual:   55 minutes
"""
from prac_06.guitar import Guitar


def main():
    print("My guitars!")
    guitars = []
    get_name = input("Name: ")

    while get_name != "":
        get_year = int(input("Year: "))
        get_cost = input("Cost: ")
        add_guitar = Guitar(get_name, get_year, get_cost)
        guitars.append(add_guitar)
        print(add_guitar, "added")
        get_name = input("Name: ")

    guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    guitars.append(Guitar("Line 6 JVT-59", 2010, 1512.90))

    if guitars:
        guitars.sort()
        print("These are my guitars:")
        for i, guitar in enumerate(guitars):
            vintage = ""
            if guitar.is_vintage():
                vintage = "(vintage)"
            print("Guitar {0}: {1.name:>20} ({1.year}), worth ${1.cost:<10} {2}".format(i + 1, guitar, vintage))
    else:
        print("No guitars ")


main()
