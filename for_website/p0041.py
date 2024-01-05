from itertools import permutations

def prime(n):
    if n < 4:
        return n == 2 or n == 3
    if n % 2 == 0:
        return False
    d = 3
    while d*d <= n:
        if n % d  == 0:
            return False
        d += 2
    return True

count = 0
largest = 0
for perm in permutations('1234'):
    n = int(''.join(perm))
    if prime(n):
        largest = max(largest,n)
        count += 1
print(f'found {count} 4 digit primes')

count = 0
for perm in permutations('1234567'):
    n = int(''.join(perm))
    if prime(n):
        largest = max(largest,n)
        count += 1
print(f'found {count} 7 digit primes')

print(largest)
