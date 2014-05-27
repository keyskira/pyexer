from math import sqrt
import time

primes = [2, 3]

def findNextPrime():
    n = primes[-1] + 2
    s = int(sqrt(n))
    while True:
        isPrime = True
        for p in primes:
            if p > s:
                break
            if n % p == 0:
                isPrime = False
                break
        if isPrime:
            primes.append(n)
            break
        n += 2
    return n


def findMaxPrimeFactor(n):
    s = int(sqrt(n))
    isPrime = True
    l = len(primes)
    factor = 1
    for p in primes:
        if p > s:
            break
        if n % p == 0:
            isPrime = False
            factor = p
            break
    if isPrime:
        while primes[-1] < s:
            p = findNextPrime()
            if n % p == 0:
                isPrime = False
                factor = p
                break
    if factor == 1:
        return n
    else:
        return findMaxPrimeFactor(n/factor)


if __name__ == '__main__':
    time.clock()
    print findMaxPrimeFactor(600851475143)
    print "Duration: %f s" % time.clock()


