class Node():
    """this is the Node class that will be used for heap data structures"""

    def __init__(self, value, parent=None):
        self.value = value
        self.parent = parent
        self.children = []

    def __str__(self):
        return "Value: " + str(self.value)

    def add_children(self, value):
        if len(self.children) < 2:
            self.children.append(value)
        else:
            # do nothing since a node cannot
            # have more than two children
            pass

    def get_parent(self):
        """It returns the parent node"""
        return self.parent

    def get_left_child(self):
        """returns the left child"""
        return self.children[0]

    def get_right_child(self):
        return self.children[1]


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
        self.root = Node(0, None)
        self.heap.append(self.root)

    def get_root(self):
        """It returns the root element of Min Heap."""
        return self.root

    def add_children(self, new_child_node_value):
        for i in range(len(self.heap)):
            # check if the current node is full (has two children)
            if len(self.heap[i].children) == 2:
                # if has 2 child than move to the next child Node by iterating
                # the loop iteration variable & check if parent is smaller than
                # the children for min heap
                continue
            elif len(self.heap[i].children) < 2:
                # if the current node has less than 2 child than add the value
                # to the current node & check if parent is smaller than the
                # children for min heap
                if self.heap[i].value <= new_child_node_value:
                    new_node = Node(new_child_node_value, self.heap[i])
                    self.heap[i].children.append(new_node)
                    self.heap.append(new_node)
                    break
                else:
                    continue  # parent value is bigger

    def update_children(self):
        pass

    def delete_children(self):
        pass

    def print_heap(self):
        pass


class MaxHeap():
    """
    pass
    """


"""
I DID NOT FINISH THIS DATA STRUCTURE BECAUSE I GOT FCKN BORED
"""
