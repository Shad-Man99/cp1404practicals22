"""
Unreliable Car Test
20/11/2022
This program tests the class UnreliableCar
"""

from prac_09.unreliable_car import UnreliableCar

car1 = UnreliableCar("Car 1", 100, 25)
print(car1)
for x in range(5):
    car1.drive(20)
    print(car1)

car2 = UnreliableCar("Car 2", 100, 75)
print(car2)
for x in range(5):
    car2.drive(20)
    print(car2)

car3 = UnreliableCar("Car 3", 100, 50)
print(car3)
for x in range(5):
    car3.drive(20)
    print(car3)
