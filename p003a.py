import library
import math

N = 600851475143

# brute force basically, factoring by numbers up to square root
largest = 0
for d in range(1, int(math.sqrt(N))+1):
    if N % d == 0:
        if library.prime(N//d): # n/d decreases so if prime, its the largest
            largest = N//d
            break
        if library.prime(d): # d is increasing
            largest = d
print(largest)

# faster algorithm, dividing out smaller prime factors
n = N
while n % 2 == 0:
    n //= 2
    print(': factor', 2)
d = 3
while d <= int(math.sqrt(n)):
    while n % d == 0:
        n //= d
        print(': factor', d)
    d += 2
print(n)
