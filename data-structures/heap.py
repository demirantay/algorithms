class Node():
    """this is the Node class that will be used for heap data structures"""

    def __init__(self, value, parent):
        self.value = value
        self.children = []

    def add_children(self, value):
        self.children.append(value)


class MinHeap():
    """
    A Min-Heap is a complete binary tree in which the value in each parent
    node is smaller than or equal to the values in the children of that node.

            5                      13
         /      \               /       \
       10        15           16         31
      /                      /  \        /  \
    30                     41    51    100   41
    """

    def __init__(self):
        self.heap = []
        self.root = self.heap[0]

    def add_children(self):
        pass


class MaxHeap():
    """
    """
