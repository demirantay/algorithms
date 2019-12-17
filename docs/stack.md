# Data Structure: `Stack`

### Explanation

In computer science, a stack is an abstract data type that serves as a collection of elements, with two principal operations:

- `push`, which adds an element to the collection, and`
- `pop`, which removes the most recently added element that was not yet removed.

The order in which elements come off a stack gives rise to its alternative name, LIFO (last in, first out). Additionally, a peek operation may give access to the top without modifying the stack. The name "stack" for this type of structure comes from the analogy to a set of physical items stacked on top of each other, which makes it easy to take an item off the top of the stack, while getting to an item deeper in the stack may require taking off multiple other items first.

Simple representation of a stack runtime with push and pop operations.

### Code Example

```python
class Stack:

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
```
