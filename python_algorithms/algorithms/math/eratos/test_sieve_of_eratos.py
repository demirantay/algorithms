import unittest
from sieve_of_eratos import eratos


class TestEratos(unittest.TestCase):

    def test_eratos_with_limit_as_10(self):
        self.assertEqual(eratos(10), True)


if __name__ == "__main__":
    unittest.main()
