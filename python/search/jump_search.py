import math


def jump_search(array, searched_element):
    """
    - Definition: Like Binary Search, Jump Search (or Block Search) is a
    searching algorithm for sorted arrays. The basic idea is to check fewer
    elements (than linear search) by jumping ahead by fixed steps or skipping
    some elements in place of searching all elements.

    - Complexity: O(√n) - because we do search by blocks of size √n.
    """

    # Step 1: Set i=0 and m = √n.
    i = 0
    m = int(math.sqrt(len(array)))
    jump_block = int(math.sqrt(len(array)))
    is_found = "None"

    # Step 2: Compare A[i] with item. If A[i] != item and A[i] < item, then
    # jump to the next block. Also, do the following: Set i = m
    # Increment m by √n

    for i in range(len(array)):
        if array[i] == searched_element:
            is_found = "Found at the index: 0"
        elif array[i] != searched_element and searched_element > array[i]:
            # Step 3: Repeat the step 2 till m < n-1
            i = jump_block
            jump_block += jump_block
        elif array[i] > searched_element:
            # Step 4: If A[i] > item, then move to the beginning of the
            # current block and perform a linear search.
            i -= m
            jump_block -= m
            for i in range(jump_block):
                if searched_element == array[i]:
                    is_found = "Found at the index: " + str(i)

        else:
            is_found = "-1"

    return is_found






a = [1, 2, 3, 4, 5, 6, 7, 8, 9,10]
print(jump_search(a, 7))
