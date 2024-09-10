import unittest
"""Max integer - Unittest"""

max_integer = __import__('6-max_integer').max_integer
class MaxInteger(unittest.TestCase):
    def test_type(self):
        test_list = [5, 4, 3]
        self.assertIsInstance(test_list, list)
    def test_element_type(self):
        test_list = [5, 4, 3]
        self.assertEqual(all(isinstance(sub, int) for sub in test_list), True)
    def test_is_max(self):
        self.assertEqual(max_integer([0, 2, 1]), 2)
    def test_type_empty_list(self):
        self.assertEqual(max_integer([]), None)

if __name__ == '__main__':
    unittest.main()
