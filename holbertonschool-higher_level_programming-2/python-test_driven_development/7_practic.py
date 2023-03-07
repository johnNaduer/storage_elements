import unittest

def add(a, b):
    return a + b

class TestAddFunction(unittest.TestCase):
    def test_add_integers(self):
        result = add(1, 2)
        self.assertEqual(result, 3)

    def test_add_floats(self):
        result = add(0.1, 0.2)
        self.assertAlmostEqual(result, 0.3, places=1)

    def test_add_integers2(self):
        result = add(4, 5)
        self.assertEqual(result, 9)

if __name__ == '__main__':
    unittest.main()
