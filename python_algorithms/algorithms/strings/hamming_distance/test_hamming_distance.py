import unittest
from hamming_distance import hamming_distance


class TestHammingDistance(unittest.TestCase):

    def test_hamming_distance_with_strings_first_example(self):
        self.assertEqual(hamming_distance("karolin", "kathrin"), 3)

    def test_hamming_distance_with_strings_second_example(self):
        self.assertEqual(hamming_distance("karolin", "kerstin"), 3)

    def test_hamming_distance_with_strings_third_example(self):
        self.assertEqual(hamming_distance("1011101", "1001001"), 2)

    def test_hamming_distance_with_strings_fourth_example(self):
        self.assertEqual(hamming_distance("2173896", "2233796"), 3)


if __name__ == "__main__":
    unittest.main()
