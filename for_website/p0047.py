num_consec = 4
num_factors = 4

sieve_size = 100000 # arbitrary starting sieve size
while True:
    print(f'trying sieve size {sieve_size}')
    answer_found = False
    # sieve for counting distinct prime factors
    sieve = [0]*sieve_size
    for i in range(2,sieve_size):
        if sieve[i] > 0: # not prime
            continue
        for j in range(i,sieve_size,i):
            sieve[j] += 1 # numbers which have this prime factor
    # search for a solution
    consec = 0 # count consecutive
    for i in range(2,sieve_size):
        if sieve[i] == num_factors:
            consec += 1
        else:
            consec = 0 # reset counter
        if consec >= num_consec:
            print(i - (num_consec - 1))
            answer_found = True
    if answer_found:
        break
    sieve_size *= 2 # double sieve size to try again
