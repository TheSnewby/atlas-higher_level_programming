#!/usr/bin/python3
import unittest
import os
import io
import sys
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestAlmostACircle(unittest.TestCase):
    # setUp is a reserved unittest function to be called before each test
    def setUp(self):
        Base._Base__nb_objects = 0

    def tearDown(self):
        if os.path.exists('Rectangle.json'):
            os.remove('Rectangle.json')
        if os.path.exists('Square.json'):
            os.remove('Square.json')

    # BASE SECTION
    def testBaseNoParameter(self):
        actual_result = Base()
        self.assertEqual(actual_result.id, 1)

    def testBaseID(self):
        actual_result = Base(2)
        self.assertEqual(actual_result.id, 2)

    def testToJsonStringSingle(self):
        list_dict = [Rectangle(1,2).to_dictionary()]
        actual_result = Base.to_json_string(list_dict)
        expected_result = '[{"x": 0, "y": 0, "id": 1, "height": 2, "width": 1}]'
        self.assertEqual(actual_result, expected_result)

    def testToJsonStringDouble(self):
        list_dict = [Rectangle(1,2).to_dictionary(), Square(3).to_dictionary()]
        actual_result = Base.to_json_string(list_dict)
        expected_result = '[{"x": 0, "y": 0, "id": 1, "height": 2, "width": 1}, {"id": 2, "x": 0, "size": 3, "y": 0}]'
        self.assertEqual(actual_result, expected_result)

    def testToJsonStringEmpty(self):
        self.assertEqual(Base.to_json_string(None), '[]')

    def testToJsonStringEmptyList(self):
        self.assertEqual(Base.to_json_string([]), '[]')

    def testSaveToFileDouble(self):
        obj1 = Rectangle(1, 2, 3, 4)
        obj2 = Rectangle(5, 5)
        Rectangle.save_to_file([obj1, obj2])
        with open ("Rectangle.json", 'r') as f:
            reading = f.read()
        self.assertIn('"width": 1', reading)

    def testSaveToFileNone(self):
        Rectangle.save_to_file(None)
        with open ("Rectangle.json", 'r') as f:
            reading = f.read()
        self.assertEqual(reading, '[]')

    def testSaveToFileEmpty(self):
        Rectangle.save_to_file([])
        with open ("Rectangle.json", 'r') as f:
            reading = f.read()
        self.assertEqual(reading, '[]')

    def testFromJsonString(self):
        json_string = '[{"x": 0, "y": 0, "id": 1, "height": 2, "width": 1}, {"id": 2, "x": 0, "size": 3, "y": 0}]'
        expected_result = [Rectangle(1,2).to_dictionary(), Square(3).to_dictionary()]
        actual_result = Base.from_json_string(json_string)
        self.assertEqual(actual_result, expected_result)

    def testFromJsonStringNone(self):
        self.assertEqual(Base.from_json_string(None), [])

    def testFromJsonStringEmptyString(self):
        self.assertEqual(Base.from_json_string(''), [])

    def testCreateRectangle(self):
        rect_dict = Rectangle(1, 2).to_dictionary()
        create_dict = Rectangle.create(**rect_dict)
        self.assertEqual(create_dict.width, 1)
        self.assertEqual(create_dict.height, 2)
        self.assertEqual(create_dict.id, 1)

    def testCreateSquare(self):
        squar_dict = Square(1).to_dictionary()
        create_dict = Square.create(**squar_dict)
        self.assertEqual(create_dict.width, 1)
        self.assertEqual(create_dict.height, 1)
        self.assertEqual(create_dict.id, 1)

    def testLoadFromFile(self):
        obj1 = Rectangle(1, 2)
        obj2 = Rectangle(3, 4)
        Rectangle.save_to_file([obj1, obj2])
        list_obj = Rectangle.load_from_file()
        self.assertIsInstance(list_obj[1], Rectangle)

    def testLoadFromFileDoesNotExist(self):
        list_obj = Rectangle.load_from_file()
        self.assertEqual(list_obj, [])

    def testSquareLoadFromFile(self):
        obj1 = Square(1, 2)
        obj2 = Square(3, 4)
        Square.save_to_file([obj1, obj2])
        list_obj = Square.load_from_file()
        self.assertIsInstance(list_obj[1], Square)

    def testSquareLoadFromFileDoesNotExist(self):
        list_obj = Square.load_from_file()
        self.assertEqual(list_obj, [])

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

    def testRectangleXNegative(self):
        self.assertRaises(ValueError, Rectangle, 2, 3, -4, 5)

    def testRectangleYNegative(self):
        self.assertRaises(ValueError, Rectangle, 2, 3, 4, -5)

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

    def testRectangleDisplay(self):
        rect = Rectangle(2, 2)
        capture = io.StringIO()
        sys.stdout = capture
        rect.display()
        expected_result = '##\n##\n'
        self.assertEqual(capture.getvalue(), expected_result)

    def testRectangleDisplayXY(self):
        rect = Rectangle(2, 2, 1, 1)
        capture = io.StringIO()
        sys.stdout = capture
        rect.display()
        expected_result = '\n ##\n ##\n'
        self.assertEqual(capture.getvalue(), expected_result)

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

    def testSquareSizeNegative(self):
        self.assertRaises(ValueError, Square, -1)

    def testSquareSizeString(self):
        self.assertRaises(TypeError, Square, "1")

    def testSquareSizeZero(self):
        self.assertRaises(ValueError, Square, 0)

    def testSquareXStr(self):
        self.assertRaises(TypeError, Square, 1, '2')

    def testSquareYStr(self):
        self.assertRaises(TypeError, Square, 1, 2, '3')

    def testSquareXNegative(self):
        self.assertRaises(ValueError, Square, 1, -1)

    def testSquareYNegative(self):
        self.assertRaises(ValueError, Square, 1, 1, -2)

    def testSquareDisplay(self):
        rect = Square(2)
        capture = io.StringIO()
        sys.stdout = capture
        rect.display()
        expected_result = '##\n##\n'
        self.assertEqual(capture.getvalue(), expected_result)

    def testSquareSaveToFileDouble(self):
        obj1 = Square(1, 3, 4)
        obj2 = Square(5)
        Square.save_to_file([obj1, obj2])
        with open ("Square.json", 'r') as f:
            reading = f.read()
        self.assertIn('"size": 1', reading)

    def testSquareSaveToFileNone(self):
        Square.save_to_file(None)
        with open ("Square.json", 'r') as f:
            reading = f.read()
        self.assertEqual(reading, '[]')

    def testSquareSaveToFileEmpty(self):
        Square.save_to_file([])
        with open ("Square.json", 'r') as f:
            reading = f.read()
        self.assertEqual(reading, '[]')

if __name__ == '__main__':
    unittest.main()