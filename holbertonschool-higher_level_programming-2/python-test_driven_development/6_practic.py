import unittest

def max_integer(list=[]):
    if len(list) == 0:
        return None
    max_value = list[0]
    for i in range(1, len(list)):
        if list[i] > max_value:
            max_value = list[i]
    return max_value

class TestMaxInteger(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(max_integer([]), None)

    def test_list_of_integers(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)
        self.assertEqual(max_integer([1, 4, 2, 3]), 4)

    def test_list_of_negative_integers(self):
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
        self.assertEqual(max_integer([-4, -3, -2, -1]), -1)
        self.assertEqual(max_integer([-1, -4, -2, -3]), -1)

if __name__ == '__main__':
    unittest.main()
