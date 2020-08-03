def merge(array_1, array_2):
    temporary_array = []



    return temporary_array


def merge_sort(array):
    if len(array) > 1:
        middle = len(array) // 2
        left_part = array[:middle]
        right_part = array[middle:]

        array_one = merge_sort(left_part)
        array_two = merge_sort(right_part)

        # sorted_array = merge(array_one, array_two)

        sorted_array = []

        i = j = k = 0

        while i < len(left_part) and j < len(right_part):
            print("hey")

        return sorted_array



print(merge_sort([50, 40, 30, 10]))
