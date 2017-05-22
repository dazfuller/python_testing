""" Test cases for sample module
"""

import unittest

from sample.primes import (approx_number_primes, is_prime)

class TestPrimeMethods(unittest.TestCase):
    """ Test the methods defined for prime numbers
    """
    def test_approx_small_values(self):
        """ Check that the method to approximate number of primes is
            working as expected
        """
        self.assertGreater(approx_number_primes(10), 4)
    
    def test_approx_larger_values(self):
        """ Determine if the method still works for slight larger values
        """
        self.assertGreater(approx_number_primes(100), 25)
    
    def test_known_primes(self):
        """ Check a number of known primes to ensure the prime evaluator
            method works
        """
        self.assertTrue(is_prime(2))
        self.assertTrue(is_prime(7))
        self.assertTrue(is_prime(997))
        self.assertTrue(is_prime(7907))
    
    def test_known_non_primes(self):
        """ Check that the prime evaluator correctly identify non-prime
            numbers as non-prime
        """
        self.assertFalse(is_prime(3))
        self.assertFalse(is_prime(93))
        self.assertFalse(is_prime(9994))
    
    def test_prime_check_nonint(self):
        """ Check that the method correctly raises an error if an invalid
            type is provided
        """
        with self.assertRaises(TypeError):
            is_prime("Invalid")
