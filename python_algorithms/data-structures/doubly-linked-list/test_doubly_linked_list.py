import unittest
from doubly_linked_list import DoublyLinkedList


class TestDoublyLinkedList(unittest.TestCase):

    def test_if_insert_head_works(self):
        d = DoublyLinkedList(0)
        d.insert_head(-1)
        self.assertEqual(d.__str__(), "[-1, 0]")

    def test_if_insert_tail_works(self):
        d = DoublyLinkedList(0)
        d.insert_tail(10)
        self.assertEqual(d.__str__(), "[0, 10]")


if __name__ == "__main__":
    unittest.main()
