# Data Structure: `Linked List`

### Explanation


### Code Example

```python
class Node:

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

  # There are more stuff such as search, remove ... I havent added them yet
```
