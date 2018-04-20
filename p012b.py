import libtkoz as lib

divisors = 500

# faster solution using a few properties
# first, compute the number of divisors by factoring
# if n = p^a * q^b * ..., (p q prime, a b exponents), divisors = (a+1)*(b+1)*...
# triangle numbers are n(n+1)/2 so the property of coprime can be used
# if n=pq, p q coprime, then divisors(n) = divisors(p) * divisors(q)
# if n odd then (n+1)/2 and n are coprime, n even --> n/2 and n+1 coprime
# this can be shown trivially with eulers gcd algorithm
# the sequence can be computing like below:
# 1*(2/2), (2/2)*3, 3*(4/2), (4/2)*5, 5*(6/2), (6/2)*7, 7*(8/2), (8/2)*9, ...
divs_odd = 1
divs_even = 1
i = 2
while True: # loop with i being later number, calculate number as i(i-1)/2
    if i % 2 == 0: # even, count factors of i/2
        divs_even = lib.divisors2(i//2)
    else: # odd, count factors of i
        divs_odd = lib.divisors2(i)
    if divs_even * divs_odd > divisors:
        print(': divisors =', divs_even * divs_odd)
        print(i * (i-1) // 2)
        break
    i += 1

