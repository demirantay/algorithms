# Data Structure: `Doubly Linked List`

### Explanation

Desc: In computer science, a doubly linked list is a linked data structure that consists of a set of sequentially linked records called nodes. Each node contains two fields, called links, that are references to the previous and to the next node in the sequence of nodes. The beginning and ending nodes' previous and next links, respectively, point to some kind of terminator, typically a sentinel node or null, to facilitate traversal of the list. If there is only one sentinel node, then the list is circularly linked via the sentinel node. It can be conceptualized as two singly linked lists formed from the same data items, but in opposite sequential orders.

The two node links allow traversal of the list in either direction. While adding or removing a node in a doubly linked list requires changing more links than the same operations on a singly linked list, the operations are simpler and potentially more efficient (for nodes other than first nodes) because there is no need to keep track of the previous node during traversal or no need to traverse the list to find the previous node, so that its link can be modified.

### Code Example

```python
class Node:

    def __init__(self, data=None, previous=None, next=None):
        self.data = data
        self.previous = previous
        self.next = next

    def __str__(self):
        return str(self.data)

    def get_data(self):
        return self.data

    def get_previous(self):
        return self.previous

    def get_next(self):
        return self.next

    def set_previous(self, new_previous):
        self.previous = new_previous

    def set_next(self, new_next):
        self.next = new_next


class DoublyLinkedList:

    def __init__(self, data):
        self.current_node = Node(data)  # creates the first node on the list
        self.head = self.current_node
        self.tail = self.current_node

    def __str__(self):
        to_string = "[" + str(self.head.data)
        current_node = self.head
        # this loop basically traverses the list
        while True:
            current_node = current_node.next
            to_string += ", " + str(current_node)
            if current_node.next is None:
                break
        to_string += "]"
        return to_string

    def insert_head(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head.previous = new_node
        self.head = new_node

    def insert_tail(self, data):
        new_node = Node(data)
        new_node.previous = self.tail
        self.tail.next = new_node
        self.tail = new_node

```
