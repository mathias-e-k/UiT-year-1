def gcd1(a, b):
    # Brute force: O(n)
    n = min(a, b)
    while n > 1:
        if a % n == 0 and b % n == 0:
            gcd = n
            return gcd
        n -= 1

def gcd(a, b):
    # Euclid algorithm: O(log n)
    print(a, b, a % b)
    if a % b == 0:
        return b
    return gcd(b, a % b)

if __name__ == "__main__":

    print(gcd(88023, 6586))