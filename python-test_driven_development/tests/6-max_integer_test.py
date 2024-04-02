#!/usr/bin/python3
"""Module de test
"""

import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Test de la fonction max_integer
    """
    def test_maxInteger(self):
        """Test equals method"""
        self.assertEqual(max_integer([1, 2, 3, 4]),4)
        self.assertEqual(max_integer([5, 2, 3, 4]),5)
        self.assertEqual(max_integer([1, 4, 3, 2]),4)
        self.assertEqual(max_integer([1, -2, 3, 4]),4)
        self.assertEqual(max_integer([-1, -2, -3, -4]),-1)
        self.assertEqual(max_integer([4]),4)
        self.assertEqual(max_integer([]),None)
        
        
        
        