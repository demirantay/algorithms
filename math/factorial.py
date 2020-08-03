def factorial(n):
    """
    Def: n mathematics, the factorial of a non-negative integer n, denoted by
    n!, is the product of all positive integers less than or equal to n. For
    example:  5! = 5 * 4 * 3 * 2 * 1 = 120
    """
    result = 1

    if n == 0:
        return result
    else:
        for i in range(1, n+1, 1):
            result *= i
        return result
