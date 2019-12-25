import unittest
from fibonacci import is_prime


class TestFibonacci(unittest.TestCase):

    def test_is_prime_with_5(self):
        self.assertEqual(is_prime(5), True)


if __name__ == "__main__":
    unittest.main()
