from Heap import Heap

def heapSort(lst):
    heap = Heap() # Create a Heap 

    # Add elements to the heap
    for v in lst:
        heap.add(v)
    # Remove elements from the heap
    for i in range(len(lst)): 
        lst[i] = heap.remove()
  
def main():
    # Min-heap
    lst = [int(i) for i in input("Enter numbers to sort: ").split()]
    heapSort(lst)
    for v in lst:
        print(v, end = " ")

main()