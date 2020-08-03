import random


def fisher_yates_shuffle(set):
    """
    The Fisher–Yates shuffle is an algorithm for generating a random
    permutation of a finite sequence—in plain terms, the algorithm shuffles
    the sequence. The algorithm effectively puts all the elements into a hat;
    it continually determines the next element by randomly drawing an element
    from the hat until no elements remain. The algorithm produces an unbiased
    permutation: every permutation is equally likely. The modern version of the
    algorithm is efficient: it takes time proportional to the number of items
    being shuffled and shuffles them in place

    Basically it just fucking shuffles a set.
    """

    for i in range(0, len(set), 1):
        random_index = random.randint(0, 9)
        temp = set[i]
        set[i] = set[random_index]
        set[random_index] = temp

    return set
