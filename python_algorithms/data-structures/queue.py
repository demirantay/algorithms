class Queue:
    """
    Data Structure: Queue
    ---
    Desc: A Queue is a linear structure which follows a particular
    order in which the operations are performed. The order is First In First
    Out (FIFO). A good example of a queue is any queue of consumers for a reso
    -urce where the consumer that came first is served first.
    """

    def __init__(self):
        self.list = []

    def __str__(self):
        return str(self.list)

    def enqueue(self, item):
        "adds a new element to the end of the list"
        self.list.append(item)

    def dequeue(self):
        "deletes the first element of the list"
        self.list.pop(0)
