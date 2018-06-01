import libtkoz as lib

ratio = 0.10 # prime ratio must get smaller than this

# brute force, test all primes in spiral, takes ~7.5 sec (i5-2540m)
step = 2 # difference between numbers in next loop
# side length is step+1 and number visited is 2*step+1 (+1 for center 1)
spiralnum = 1 # number to test for primality
primes = 0
while True:
    # try 4 corner numbers in next loop
    for i in range(4):
        spiralnum += step
        if lib.prime(spiralnum): primes += 1
    if primes / (2*step+1) < ratio: # prime ratio small enough
        print(step+1)
        break
    step += 2
