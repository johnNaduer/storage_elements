import unittest

def square(x):
    """Return the square of a number."""
    return x * x

class TestSquare(unittest.TestCase):
    """Tests for the `square` function."""

    def test_square(self):
        """Test that the square of a number is correct."""
        self.assertEqual(square(2), 4)
        self.assertEqual(square(-2), 4)
        self.assertEqual(square(0), 0)

if __name__ == '__main__':
    unittest.main()
