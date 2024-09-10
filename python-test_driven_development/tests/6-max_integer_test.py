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
    def test_max_at_middle(self):
        self.assertEqual(max_integer([0, 2, 1]), 2)
    def test_type_empty_list(self):
        self.assertEqual(max_integer([]), None)
    def test_max_at_end(self):
        self.assertEqual(max_integer([1, 2, 3]), 3)
    def test_max_at_beginning(self):
        self.assertEqual(max_integer[3, 2, 1], 3)
    def test_one_negative_in_list(self):
        self.assertEqual(max_integer(-5, 1, 2), 2)
    def test_all_negatives_in_list(self):
        self.assertEqual(max_integer([-1, -2, -3]), -1)
    def test_only_one_element(self):
        self.assertEqual(max_integer[1], 1)

if __name__ == '__main__':
    unittest.main()
