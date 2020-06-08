def fibonacci(n):
    """
    Def: In mathematics, the Fibonacci numbers are the numbers in the following
    integer sequence, called the Fibonacci sequence, and characterized by the
    fact that every number after the first two is the sum of the two preceding
    ones:  `0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ...`
    """

    fibonacci_sequence = [0, 1]

    for i in range(0, n, 1):
        next = fibonacci_sequence[i] + fibonacci_sequence[i + 1]
        fibonacci_sequence.append(next)

    return fibonacci_sequence[:-2]
