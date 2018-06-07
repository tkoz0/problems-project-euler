import libtkoz as lib

sumways = 5000

# dynamic programming

maxprime = 32
while True: # increase prime limit until finding a solution
    ways = [0] * (maxprime + 1)
    plist = lib.list_primes2(maxprime)
    ways[0] = 1 # 1 way, nothing, for when first prime selected is itself
    ways[1] = 0 # not prime, no smaller primes
    for p in plist: # add how many ways i=p+k --> k as sum of primes <= p
        for i in range(p,maxprime+1):
            ways[i] += ways[i-p]
    solution = -1
    for i,w in enumerate(ways): # find satisfying number
        if w > sumways:
            solution = i
            break
    if solution != -1: # found a satisfying number
        print(':', solution, 'can be expressed in', ways[solution], 'ways')
        print(solution)
        break
    maxprime *= 2
