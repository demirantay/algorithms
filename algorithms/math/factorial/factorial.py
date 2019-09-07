def factorial(number):
    '''
    Returns the factorial of the given parameter
    '''
    result = 1

    for i in range(0, number, 1):
        result *= i+1

    return result
