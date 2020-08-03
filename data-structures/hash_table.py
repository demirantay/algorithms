#
#   You can use this as reference but it is not perfect just remember:
#    https://coderbook.com/@marcus/how-to-create-a-hash-table-from-scratch-in-python/
#
#
# INSTEAD OF CRAMMIG EERYTHING INTO A CLASS HAVE A KeyNode and a ValueNode and
# have a link between them. So that it is easy because just by searching key will
# ive the ValueNode thorgh the their linkage


class HashTable:
    """
    In computing, a hash table (hash map) is a data structure which implements
    an associative array abstract data type, a structure that can map keys to
    values. A hash table uses a hash function to compute an index into an array
    of buckets or slots, from which the desired value can be found

    Ideally, the hash function will assign each key to a unique bucket, but
    most hash table designs employ an imperfect hash function, which might
    cause hash collisions where the hash function generates the same index for
    more than one key. Such collisions must be accommodated in some way.
    """

    def __init__(self, capacity=100):
        self.hash_table = [None] * capacity

    def hash_func(self, key):
        """"Get the index of our array for a specific string key"""

    def add(self, key, value):
        """add a value and a key pair to the hashtable"""
        pass

    def get(self, key):
        """get value by key"""

    def is_full(self):
        """deternimes if the table is full"""

    def double(self):
        """doubles the hash table size"""
