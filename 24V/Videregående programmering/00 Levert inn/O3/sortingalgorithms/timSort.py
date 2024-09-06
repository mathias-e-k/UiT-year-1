from tim_insertion_sort import insertion_sort
from mergeSort import merge
def timSort(array):
    min_run = 32
    n = len(array)

    # Start by slicing and sorting small portions of the
    # input array. The size of these slices is defined by
    # your `min_run` size.
    for i in range(0, n, min_run):
        insertion_sort(array, i, min((i + min_run - 1), n - 1))

    # Now you can start merging the sorted slices.
    # Start from `min_run`, doubling the size on
    # each iteration until you surpass the length of
    # the array.
    size = min_run
    while size < n:
        # Determine the arrays that will
        # be merged together
        for start in range(0, n, size * 2):
            # Compute the `midpoint` (where the first array ends
            # and the second starts) and the `endpoint` (where
            # the second array ends)
            midpoint = start + size - 1
            end = min((start + size * 2 - 1), (n-1))

            # Merge the two subarrays.
            # The `left` array should go from `start` to
            # `midpoint + 1`, while the `right` array should
            # go from `midpoint + 1` to `end + 1`.
            left = array[start:midpoint + 1]
            right = array[midpoint + 1:end + 1]
            merged_array = [0] * (len(left) + len(right))
            merge(list1=left, list2=right, temp=merged_array)

            # Finally, put the merged array back into
            # your array
            array[start:start + len(merged_array)] = merged_array

        # Each iteration should double the size of your arrays
        size *= 2

    return array

if __name__ == "__main__":
    lst = [5, 3, 1, 6, 2, 9, 8, 22, 12, 10, 15, 27, 40, 32]
    timSort(lst)
    print(lst)