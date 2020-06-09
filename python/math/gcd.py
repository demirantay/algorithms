def gcd(a, b):
    """
    Def: In mathematics, the Euclidean algorithm, or Euclid's algorithm, is an
    efficient method for computing the greatest common divisor (GCD) of two
    numbers, the largest number that divides both of them without leaving a
    remainder.
    """

    if a == 0:
        return b

    return gcd(b % a, a)
