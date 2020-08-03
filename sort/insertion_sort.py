def swap(a, b):
    temp = a
    a = b
    b = temp


def insertion_sort(array):
    """Implementation of the Insertion Sort algorithm"""

    for i in range(len(array)):
        for j in range(len(array)):
            if array[i] < array[j]:
                # swap
                temporary = array[i]
                array[i] = array[j]
                array[j] = temporary
            else:
                continue

    return array
