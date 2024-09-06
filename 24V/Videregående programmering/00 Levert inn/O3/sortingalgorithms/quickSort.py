import random
def quickSort(lst):
    quicksort_helper(lst, 0, len(lst) - 1)

def quicksort_helper(lst, first, last):
    if last > first:
        pivot_index = partition(lst, first, last)
        quicksort_helper(lst, first, pivot_index - 1)
        quicksort_helper(lst, pivot_index + 1, last)

def partition(lst, first, last):
    mid = (first + last) // 2
    if lst[mid] < lst[last]:
        lst[mid], lst[last] = lst[last], lst[mid]
    if lst[first] < lst[last]:
        lst[first], lst[last] = lst[last], lst[first]
    if lst[mid] < lst[first]:
        lst[mid], lst[first] = lst[first], lst[mid]
    pivot = lst[first]
    low = first + 1
    high = last

    while high > low:
        while low <= high and lst[low] <= pivot:
            low += 1
        while low <= high and lst[high] >= pivot:
            high -= 1
        if high > low:
            lst[high], lst[low] = lst[low], lst[high]
    
    # move pivot to correct position:
    while high > first and lst[high] >= pivot:
        high -= 1

    if pivot > lst[high]:
        lst[first], lst[high] = lst[high], pivot
        return high     # return position of pivot
    else:
        return first

if __name__ == "__main__":
    AMOUNT_OF_NUMBERS = 30
    lst = [random.randint(1, 20 + AMOUNT_OF_NUMBERS) for _ in range(AMOUNT_OF_NUMBERS)]
    quickSort(lst)

    print(lst)