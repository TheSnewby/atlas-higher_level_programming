#!/usr/bin/python3
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestAlmostACircle(unittest.TestCase):
    # setUp is a reserved unittest function to be called before each test
    def setUp(self):
        Base._Base__nb_objects = 0

    # BASE SECTION
    def testBaseNoParameter(self):
        actual_result = Base()
        self.assertEqual(actual_result.id, 1)

    def testBaseID(self):
        actual_result = Base(2)
        self.assertEqual(actual_result.id, 2)

    # RECTANGLE SECTION
    def testRectangleWidth(self):
        actual_result = Rectangle(2, 3).width
        expected_result = 2
        self.assertEqual(actual_result, expected_result)

    def testRectangleHeight(self):
        actual_result = Rectangle(2, 3).height
        expected_result = 3
        self.assertEqual(actual_result, expected_result)

    def testRectangleID(self):
        actual_result = Rectangle(2, 3).id
        expected_result = 1
        self.assertEqual(actual_result, expected_result)

    def testRectangleX(self):
        actual_result = Rectangle(2, 3, 4).x
        expected_result = 4
        self.assertEqual(actual_result, expected_result)

    def testRectangleY(self):
        actual_result = Rectangle(2, 3, y=5).y
        expected_result = 5
        self.assertEqual(actual_result, expected_result)

    def testRectangleWidthString(self):
        self.assertRaises(TypeError, Rectangle, '2', 3, 0, 5)

    def testRectangleWidthNegative(self):
        self.assertRaises(ValueError, Rectangle, -1, 3, 0, 5)

    def testRectangleHeightString(self):
        self.assertRaises(TypeError, Rectangle, 2, '3', 0, 5)

    def testRectangleHeightNegative(self):
        self.assertRaises(ValueError, Rectangle, 2, -3, 0, 5)

    def testRectangleXString(self):
        self.assertRaises(TypeError, Rectangle, 2, 3, "4")

    def testRectangleYString(self):
        self.assertRaises(TypeError, Rectangle, 2, 3, 4, "5")

    def testRectangleHeightZero(self):
        self.assertRaises(ValueError, Rectangle, 2, 0, 0, 5)

    def testRectangleWidthZero(self):
        self.assertRaises(ValueError, Rectangle, 0, 3, 0, 5)

    def testRectangleWidthSetter(self):
        test_rect = Rectangle(2, 3)
        test_rect.width = 4
        actual_result = test_rect.width
        expected_result = 4
        self.assertEqual(actual_result, expected_result)

    def testRectangleHeightSetter(self):
        test_rect = Rectangle(2, 3)
        test_rect.height = 4
        actual_result = test_rect.height
        expected_result = 4
        self.assertEqual(actual_result, expected_result)

    def testRectangleXSetter(self):
        test_rect = Rectangle(2, 3)
        test_rect.x = 4
        actual_result = test_rect.x
        expected_result = 4
        self.assertEqual(actual_result, expected_result)

    def testRectangleYSetter(self):
        test_rect = Rectangle(2, 3)
        test_rect.y = 4
        actual_result = test_rect.y
        expected_result = 4
        self.assertEqual(actual_result, expected_result)

    def testRectangleArea(self):
        actual_result = Rectangle(2, 3).area()
        expected_result = 6
        self.assertEqual(actual_result, expected_result)

    def testRectangleUpdateArgs(self):
        args = [5, 1, 2, 3, 4]
        actual_result = Rectangle(2, 3)
        actual_result.update(*args)
        expected_result = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(actual_result.id, expected_result.id)
        self.assertEqual(actual_result.width, expected_result.width)
        self.assertEqual(actual_result.height, expected_result.height)
        self.assertEqual(actual_result.x, expected_result.x)
        self.assertEqual(actual_result.y, expected_result.y)

    # def testRectangleDisplay(self):
    #     actual_result = Rectangle(2, 1).display()
    #     expected_result = '##'
    #     self.assertEqual(actual_result, expected_result)

    def testRectangleToDictionary(self):
        actual_result = Rectangle(1, 2).to_dictionary()
        expected_result = {'x':0,'y':0,'id':1,'height':2,'width':1}
        self.assertEqual(actual_result, expected_result)

    def testRectangleStr(self):
        actual_result = Rectangle(1, 2).__str__()
        expected_result = '[Rectangle] (1) 0/0 - 1/2'
        self.assertEqual(actual_result, expected_result)

    # SQUARE SECTION
    def testSquareWidth(self):
        actual_result = Square(1).width
        expected_result = 1
        self.assertEqual(actual_result, expected_result)

    def testSquareHeight(self):
        actual_result = Square(1).height
        expected_result = 1
        self.assertEqual(actual_result, expected_result)

    def testSquareID(self):
        actual_result = Square(2).id
        expected_result = 1
        self.assertEqual(actual_result, expected_result)

    def testSquareX(self):
        actual_result = Square(1, 2).x
        expected_result = 2
        self.assertEqual(actual_result, expected_result)

    def testSquareY(self):
        actual_result = Square(1, 2, 3).y
        expected_result = 3
        self.assertEqual(actual_result, expected_result)

    def testSquareXSetter(self):
        testSquare = Square(1, 2)
        testSquare.x = 3
        actual_result = testSquare.x
        expected_result = 3
        self.assertEqual(actual_result, expected_result)

    def testSquareYSetter(self):
        testSquare = Square(1, 2, 3)
        testSquare.y = 4
        actual_result = testSquare.y
        expected_result = 4
        self.assertEqual(actual_result, expected_result)

    def testSquareSTR(self):
        actual_result = Square(1).__str__()
        expected_result = '[Square] (1) 0/0 - 1'
        self.assertEqual(actual_result, expected_result)

    def testSquareUpdateArgs(self):
        args = [5, 2, 3, 4]
        actual_result = Square(1)
        actual_result.update(*args)
        expected_result = Square(2, 3, 4, 5)
        self.assertEqual(actual_result.id, expected_result.id)
        self.assertEqual(actual_result.width, expected_result.width)
        self.assertEqual(actual_result.height, expected_result.height)
        self.assertEqual(actual_result.x, expected_result.x)
        self.assertEqual(actual_result.y, expected_result.y)

    def testSquareToDictionary(self):
        actual_result = Square(1, 2, 3, 4).to_dictionary()
        expected_result = {'id':4, 'x':2, 'size':1, 'y':3}
        self.assertEqual(actual_result, expected_result)

if __name__ == '__main__':
    unittest.main()