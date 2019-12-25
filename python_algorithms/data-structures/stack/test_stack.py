import unittest
from stack import Stack


class TestStack(unittest.TestCase):

    def test_if_push_works(self):
        s = Stack()
        s.push(10)
        s.push(20)
        self.assertEqual(s.list, [10, 20])

    def test_if_pop_works(self):
        s = Stack()
        s.push(10)
        s.push(20)
        s.pop()
        self.assertEqual(s.list, [10])

    def test_if_peek_works(self):
        s = Stack()
        s.push(10)
        s.push(20)
        self.assertEqual(s.peek(), 20)


if __name__ == "__main__":
    unittest.main()
