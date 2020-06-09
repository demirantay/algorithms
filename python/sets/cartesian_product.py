def cartesian_product(set1, set2):
    """
    Desc: In set theory a Cartesian product is a mathematical operation that
    returns a set (or product set or simply product) from multiple sets. That
    is, for sets A and B, the Cartesian product A × B is the set of all ordered
    pairs (a, b) where a ∈ A and b ∈ B.

    For reference you can visit Wikipedia
    """
    cartesian_set = []

    for i in range(0, len(set1), 1):
        for j in range(0, len(set2), 1):
            cartesian_set.append([set1[i], set2[j]])

    return cartesian_set
    
