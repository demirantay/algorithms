def linear_search(array, n):
    """
    - Definition - In computer science, linear search or sequential search is a
    method for finding a target value within a list. It sequentially checks
    each element of the list for the target value until a match is found or
    until all the elements have been searched. Linear search runs in at worst
    linear time and makes at most n comparisons, where n is the length of the
    list.

    Comlexity: Time Complexity: O(n) - since in worst case we're checking each
               element exactly once.


    """
    is_found = False

    for i in array:
        if i == n:
            is_found = True
        else:
            continue

    return is_found
