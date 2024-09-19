#!/usr/bin/python3
import unittest
from base import Base
from rectangle import Rectangle
from square import Square

class TestAlmostACircle(unittest.TestCase):
    def testBase(self):
        actual_result = Base()
        self.assertEqual(actual_result.id, 1)


if __name__ == '__main__':
    unittest.main()