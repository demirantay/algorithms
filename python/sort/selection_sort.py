def selection_sort(array):
    """
    Def: Selection sort is a sorting algorithm, specifically an in-place
         comparison sort. It has O(n2) time complexity, making it inefficient
         on large lists, and generally performs worse than the similar
         insertion sort. Selection sort is noted for its simplicity, and it has
         performance advantages over more complicated algorithms in certain
         situations, particularly where auxiliary memory is limited.

    Complexity: Best: n^2 | Average: n^2 | Worst: n^2
    """
    for i in range(0, len(array), 1):
        starting_index = i

        for j in range(i, len(array), 1):
            if array[starting_index] > array[j]:
                starting_index = j

        # swapping the found element
        array[i], array[starting_index] = array[starting_index], array[i]

    return array
