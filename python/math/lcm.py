from gcd import gcd


def lcm(a, b):
    """
    In arithmetic and number theory, the least common multiple, lowest common
    multiple, or smallest common multiple of two integers a and b, usually
    denoted by LCM(a, b), is the smallest positive integer that is divisible
    by both a and b. Since division of integers by zero is undefined, this
    definition has meaning only if a and b are both different from zero.
    However, some authors define lcm(a,0) as 0 for all a, which is the result
    of taking the lcm to be the least upper bound in the lattice ofdivisibility

    algorithm: lcm(a, b) = |a * b| / gcd(a, b)
    """

    return abs(a * b) / gcd(a, b)


print(lcm(4, 6))
