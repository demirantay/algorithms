import unittest
from factorial import factorial


class TestFactorial(unittest.TestCase):

    def test_factorial_of_3(self):
        self.assertEqual(factorial(3), 6)

    def test_factorial_of_5(self):
        self.assertEqual(factorial(5), 120)

    def test_factorial_of_7(self):
        self.assertEqual(factorial(7), 5040)


if __name__ == "__main__":
    unittest.main()
