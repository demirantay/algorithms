class Stack:
    """
    Data Structure: Stack
    ---
    Desc: In computer science, a stack is an abstract data type that
    serves as a collection of elements, with two principal operations:

    push, which adds an element to the collection, and
    pop, which removes the most recently added element that was not yet removed
    """

    def __init__(self):
        self.list = []

    def __str__(self):
        return str(self.list)

    def push(self, item):
        """Adds an item to the top of the collection"""
        self.list.append(item)

    def pop(self):
        """Removes the item at the top of the collection"""
        self.list.pop(len(self.list) - 1)

    def peek(self):
        """ returns you the top item of the stack"""
        return self.list[len(self.list) - 1]
