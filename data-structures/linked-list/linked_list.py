class Node:
    """
    Linked List Nodes have two parts one is the "data" and the other is "next".
    The data as you can imagine just holds the data value and the next is a
    pointer to the next node in the sequence
    """

    def __init__(self, data=None, next=None):
        self.data = data
        self.next_node = next

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next


class LinkedList:
    """
    Data Structure: Linked List
    ---
    Desc: In computer science, a linked list is a linear collection of data
    elements, in which linear order is not given by their physical placement
    in memory. Instead, each element points to the next. It is a data structure
    consisting of a group of nodes which together represent a sequence. Under
    the simplest form, each node is composed of data and a reference (in other
    words, a link) to the next node in the sequence
    """

    def __init__(self, head=None):
        self.head = head

    def __str__(self):
        pass

    def add(self, value):
        """ Adds a new item to the 'tail' of the seqeuence """
        new_node = Node(value)
        new_node.set_next(self.head)
        self.head = new_node

    def size(self):
        """ Returns you the size of the linked list """
        current_node = self.head
        count = 0
        while (current_node):
            count += 1
            current_node = current_node.get_next()
        return count

    def search(self, value):
        """ Checks for the searched value in the list """
        current_node = self.head
        found = False
        while (current_node and found is False):
            if (current_node.get_data() == value):
                found = True
            else:
                current_node.get_next()
        if (current_node is None):
            raise ValueError("Data is not in the list")
        return found

    def remove(self):
        """ a"""
