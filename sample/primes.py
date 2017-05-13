""" Defines a number of methods for testing
"""

#pylint: disable=C0303

from math import (floor, log, sqrt)

def approx_number_primes(value):
    """ Returns the approximate number of primes below a given
        input

        Args:
        value -- the value to approximate up to
    """
    return floor((value / log(value)) * (1 + (1.2762 / log(value))))

def is_prime(value):
    """ Determines if a given value is a prime number

        Args:
        value -- The value to evaluate
    """
    if not isinstance(value, int):
        raise TypeError("value should be of type int")
    
    if value == 2:
        return True
    elif value < 2 or value % 2 == 0:
        return False
    
    limit = int(floor(sqrt(value)))
    for i in range(3, limit + 1, 2):
        if value % i == 0:
            return False
    
    return True
