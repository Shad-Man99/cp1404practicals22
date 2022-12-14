"""
Estimate: 25 minutes
Actual:  15 minutes
"""
from prac_09.silver_service_taxi import SilverServiceTaxi


def main():
    """Test SilverServiceTaxi."""
    taxi = SilverServiceTaxi("Test", 100, 2)
    taxi.drive(18)
    print(taxi)
    print("${:2f}".format(taxi.get_fare()))


main()
