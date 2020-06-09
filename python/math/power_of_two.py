def is_power_of_two(n):
    """
    Desc: Given a positive integer, write a function to find if it is a power
    of two or not.

    Naive solution: In naive solution we just keep dividing the number by two
    unless the number becomes 1 and every time we do so we check that remainder
    after division is always 0. Otherwise the number can't be a power of two.
    """
    is_power_of_two = None

    while n > 1:
        if n % 2 == 0:
            is_power_of_two = True
        else:
            is_power_of_two = False

        n = n / 2

    return is_power_of_two
