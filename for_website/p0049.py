from itertools import combinations_with_replacement,permutations

# sieve for 4 digit primes
prime = [True]*10000
prime[0] = prime[1] = False
for p in range(2,10000):
    if p*p >= 10000:
        break
    for i in range(p*p,10000,p):
        prime[i] = False

given = (1487,4817,8147)
solutions = []

for digits in combinations_with_replacement(range(10),4):
    numbers_set = set()
    for a,b,c,d in permutations(digits):
        if a == 0: # only consider 4 digit numbers
            continue
        p = 1000*a + 100*b + 10*c + d
        if prime[p]:
            numbers_set.add(1000*a + 100*b + 10*c + d)
    numbers_list = sorted(numbers_set)
    # try to form an arithmetic sequence
    for i in range(len(numbers_list)):
        for j in range(i+1,len(numbers_list)):
            d = numbers_list[j] - numbers_list[i]
            if (numbers_list[j] + d) in numbers_set:
                seq = (numbers_list[i],numbers_list[j],numbers_list[j]+d)
                print(seq)
                solutions.append(seq)

for sol in solutions:
    if sol != given:
        print(''.join(map(str,sol)))
