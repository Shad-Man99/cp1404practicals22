"""
Unreliable Car
20/11/2022
This class inherits from Car and represents an unreliable car object.
"""

from prac_09.car import Car
import random


class UnreliableCar(Car):
    """Unreliable Car class."""

    def __init__(self, name="", fuel=0, reliability=100):
        """Initialise class."""
        super().__init__(name, fuel)
        self.reliability = reliability

    def __str__(self):
        """Define rules for printing class objects."""
        return super().__str__() + " reliability={}".format(self.reliability)

    def drive(self, distance):
        """Drive the unreliable car if it doesn't break down."""
        if random.randint(0, 100) < self.reliability:
            return super().drive(distance)
        else:
            return 0
