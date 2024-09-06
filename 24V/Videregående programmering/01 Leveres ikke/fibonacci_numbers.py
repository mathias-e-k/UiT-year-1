# Fibonacci numbers using dynamic programming

cache = [0, 1]
def fib(n):
    # recursive with dynamic programming: O(n)
    if n < len(cache):
        return cache[n]
    output = fib(n-1) + fib(n-2)
    cache.append(output)
    return output

def fib2(n):
    # recursive without dynamic programming: O(2^n)
    if n < 2:
        return n
    return fib2(n-1) + fib2(n-2)

if __name__ == "__main__":
    for i in range(0,4):
        print(fib(i))

    