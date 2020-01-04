def bubble_sort(array):
    """
    Def: Bubble sort, sometimes referred to as sinking sort, is a simple
         sorting algorithm that repeatedly steps through the list to be sorted,
         compares each pair of adjacent items and swaps them if they are in the
         wrong order (ascending or descending arrangement). The pass through
         the list is repeated until no swaps are needed, which indicates that
         the list is sorted.

    Complexity: Best: n | Average: n^2 | Worst: n^2
    """
    swapped = False

    for i in range(0, len(array) - 1, 1):
        for j in range(0, len(array) - 1, 1):
            if array[j] > array[j+1]:
                # swap the elements
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp
                swapped = True
        if swapped is False:
            break

    return array
