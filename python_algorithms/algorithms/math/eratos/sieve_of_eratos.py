def eratos(n):
    """
    The Sieve of Eratosthenes is an algorithm for finding all prime numbers
    up to some limit n
    """
    prime_numbers = []

    for i in range(1, n, 1):
        if i == 1:
            prime = False
        elif i == 2 or i == 3:
            prime = True
            prime_numbers.append(i)
        elif i % 3 == 0 or i % 2 == 0 or i % 5 == 0 or i % 7 == 0:
            prime = False
        else:
            prime = True
            prime_numbers.append(i)

    return prime_numbers


print(eratos(10))
