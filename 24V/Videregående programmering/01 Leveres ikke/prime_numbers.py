def primes(n):
    # efficient algorithm for finding all primes <= n
    found_primes = []
    number = 2
    square_root = 1

    while number <= n:
        isPrime = True

        if square_root*square_root < number:
            square_root += 1
        
        k = 0
        while k < len(found_primes) and found_primes[k] <= square_root:
            if number % found_primes[k] == 0:
                isPrime = False
                break
            k += 1
        
        if isPrime:
            found_primes.append(number)
        
        number += 1
    return found_primes

if __name__ == "__main__":
    print(primes(1000))