import libtkoz as lib

limit = 10000

# brute force loop, a = divs(a) and divs(divs(a)) = a
# subtract number itself since these sum all divisors, not only proper ones
amicable = 0
for a in range(2, limit):
    sum_a = lib.sum_divisors1(a) - a
    if sum_a > a: # a < its divisor sum order
        sum_b = lib.sum_divisors1(sum_a) - sum_a
        if sum_b == a:
            print(': pair', (a, sum_a))
            amicable += a
            if sum_a < limit: amicable += sum_a
print(amicable)

# generate a cache of divisor sums, more speed at higher memory cost
# for all numbers under limit/2, add them to the sums for their multiples
cache = [1] * limit # 1 divides everything
for d in range(2, limit//2):
    for i in range(2*d, limit, d):
        cache[i] += d
# search cache similarly
amicable = 0
for a in range(2, limit):
    if a < cache[a]: # one order
        if cache[a] < limit and cache[cache[a]] == a:
            print(': pair', (a, cache[a]))
            amicable += a + cache[a]
        else:
            sum_a = lib.sum_divisors2(cache[a]) - cache[a]
            if sum_a == a:
                print(': pair', (a, sum_a))
                amicable += a
print(amicable)

