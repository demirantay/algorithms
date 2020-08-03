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


class HashTable:

    def __init__(self, capacity=100):
        self.hash_table = [None] * capacity

    def hash_func(self, key):
        """"Get the index of our array for a specific string key"""
        return key % len(self.hash_table)

    def add(self, key, value):
        """add a value and a key pair to the hashtable"""
        hash_key = hash_func(key)
        self.hash_table[hash_key] = value

    def get(self, key):
        """get value by key"""
        pass

    def is_full(self):
        """deternimes if the table is full"""
        pass

    def double(self):
        """doubles the hash table size"""
        pass



"""
I DID NOT FINISH THIS DATA STRUCTURE BECAUSE I GOT FCKN BORED
"""
