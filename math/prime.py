def is_prime(n):
    """
    Def: A prime number (or a prime) is a natural number greater than 1 that
    cannot be formed by multiplying two smaller natural numbers. A natural
    number greater than 1 that is not prime is called a composite number.
    For example, 5 is prime because the only ways of writing it as a product,
    1 × 5 or 5 × 1, involve 5 itself. However, 6 is composite because it is the
    product of two numbers (2 × 3) that are both smaller than 6.
    """

    if n == 0 or n < 0:
        return False
    elif n == 1 or n == 2 or n == 3:
        return True
    else:
        # if n does not have a remainder when divided by 2 or 3
        # then it means n is a composite number. If it has a remainder
        # then the number is a prime number.
        if n % 2 == 0 or n % 3 == 0:
            return False
        else:
            return True
