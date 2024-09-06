import random

def radixSort(lst: list[int]):
    buckets = [[] for _ in range(10)]
    max_value = max(lst)
    exp = 1
    while exp < max_value:
        while lst:
            num = lst.pop()
            radix_index = (num // exp) % 10
            buckets[radix_index].append(num)
        for bucket in buckets:
            while bucket:
                lst.append(bucket.pop())
        exp *= 10



lst = [random.randint(0, 2000) for _ in range(20)]
radixSort(lst)
print("Sorted:", lst)