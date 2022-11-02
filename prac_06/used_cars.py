"""
Estimate: 20 minutes
Actual:   25 minutes
"""

from prac_06.car import Car


def main():
    my_car = Car(180)
    my_car.drive(30)
    print(f"Car has fuel: {my_car.fuel} units of fuel")
    print(my_car)

    limo = Car("Limo", 100)
    limo.add_fuel(20)
    limo.drive(115)
    print(limo)


main()
