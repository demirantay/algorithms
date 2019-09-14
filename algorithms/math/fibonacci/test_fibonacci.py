import unittest
from fibonacci import fibonacci


class TestFibonacci(unittest.TestCase):

    def test_fibonacci_sequence_with_5_numbers(self):
        self.assertEqual(fibonacci(5), [0, 1, 1, 2, 3])

    def test_fibonacci_sequence_with_7_numbers(self):
        self.assertEqual(fibonacci(7), [0, 1, 1, 2, 3, 5, 8])

    def test_fibonacci_sequence_with_9_numbers(self):
        self.assertEqual(fibonacci(9), [0, 1, 1, 2, 3, 5, 8, 13, 21])


if __name__ == "__main__":
    unittest.main()
