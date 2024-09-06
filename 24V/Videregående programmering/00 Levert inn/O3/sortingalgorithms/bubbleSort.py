def bubbleSort(lst):
    needNextPass = True
    
    k = 1
    while k < len(lst) and needNextPass:
        # lst may be sorted and next pass not needed
        needNextPass = False
        for i in range(len(lst) - k): 
            if lst[i] > lst[i + 1]:
                # swap lst[i] with lst[i + 1]
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
                needNextPass = True # Next pass still needed

        k += 1 # The elements after index k are sorted

def main():
    lst = [2, 3, 2, 5, 6, 1, -2, 3, 14, 12]
    bubbleSort(lst)
    for v in lst:
        print(v, end = " ")
if __name__ == "__main__":
    main()