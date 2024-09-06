def mergeSort(lst):
    if len(lst) > 1:
        # Merge sort the first half
        firstHalf = lst[ : len(lst) // 2]
        mergeSort(firstHalf)

        # Merge sort the second half
        secondHalf = lst[len(lst) // 2 : ]
        mergeSort(secondHalf)

        # Merge firstHalf with secondHalf into lst
        merge(firstHalf, secondHalf, lst)

# Merge two sorted lists */
def merge(list1, list2, temp):
    current1 = 0  # Current index in list1
    current2 = 0  # Current index in list2
    current3 = 0  # Current index in temp

    while current1 < len(list1) and current2 < len(list2):
        if list1[current1] < list2[current2]:
            temp[current3] = list1[current1]
            current1 += 1
            current3 += 1
        else:
            temp[current3] = list2[current2]
            current2 += 1
            current3 += 1

    while current1 < len(list1):
        temp[current3] = list1[current1]
        current1 += 1
        current3 += 1

    while current2 < len(list2):
        temp[current3] = list2[current2]
        current2 += 1
        current3 += 1

def main():
    lst = [2, 3, 2, 5, 6, 1, -2, 3, 14, 12]
    mergeSort(lst)
    for v in lst:
        print(v, end = " ")
if __name__ == "__main__":
    main()