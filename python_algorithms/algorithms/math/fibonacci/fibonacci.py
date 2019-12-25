def fibonacci(number):
    '''
    this function returns you a list of fibonacci sequenced elements. The length
    of the array is determined by the number given in the parameter
    '''
    fib_array = [0, 1]

    for i in range(0, number - 2, 1):
        new_member = fib_array[i] + fib_array[i + 1]
        fib_array.append(new_member)

    return fib_array
