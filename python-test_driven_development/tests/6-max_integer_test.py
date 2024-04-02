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
        
        
        