import unittest
from queue import Queue


class TestQueue(unittest.TestCase):

    def test_if_enqueue_works(self):
        q = Queue()
        q.enqueue(10)
        q.enqueue(50)
        self.assertEqual(q.list, [10, 50])

    def test_if_dequeue_works(self):
        q = Queue()
        q.enqueue(10)
        q.enqueue(50)
        q.dequeue()
        self.assertEqual(q.list, [50])
        

if __name__ == "__main__":
    unittest.main()
