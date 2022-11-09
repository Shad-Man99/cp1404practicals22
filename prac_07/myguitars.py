from prac_06.guitar import Guitar


def main():
    guitars = []
    guitar_input(guitars)
    in_file = open('guitars.csv', 'r')

    for line in in_file:
        parts = line.strip().split(',')
        guitar = Guitar(parts[0], int(parts[1]), float(parts[2]))
        guitars.append(guitar)
    in_file.close()

    guitars.sort()
    save_to_file(guitars)


def guitar_input(guitars):
    guitar_name = input("Name: ")
    while guitar_name != "":
        guitar_year = int(input("Year: "))
        guitar_cost = float(input("Cost: $"))
        new_guitar = Guitar(guitar_name, guitar_year, guitar_cost)
        guitars.append(new_guitar)
        print(f"{new_guitar} added.")
        guitar_name = input("Name: ")


def save_to_file(guitars):
    out_file = open("guitars.csv", 'w')
    for guitar in guitars:
        print(f"{guitar.name},{guitar.year},{guitar.cost}", file=out_file)
    out_file.close()


main()
