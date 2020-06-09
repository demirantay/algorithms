from prime import is_prime


def sieve_of_erat(n):
    """
    The Sieve of Eratosthenes is an algorithm for finding all prime numbers up
    to some limit `n`. It is attributed to Eratosthenes of Cyrene, an ancient
    Greek mathematician.
    """
    prime_numbers_container = []

    for i in range(0, n+1, 1):
        prime_value = is_prime(i)
        if prime_value is True:
            prime_numbers_container.append(i)

    return prime_numbers_container
