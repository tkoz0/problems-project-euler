import libtkoz as lib

limit = 10**14

# recursively append digits to right to build right truncatable harshad numbers
# takes ~1.6 sec (cpython / i5-2540m) (faster with miller rabin test)

# parameters are number and digit sum
hsum = 0 # sum of harshad numbers, right truncatable, and strong
def recurse(num,dsum): # assume arguments satisfy num % dsum == 0
    global hsum, limit
    if num*10 >= limit: return
    if num % dsum == 0: # harshad number
        if lib.prime(num//dsum): # also strong harshad number
            num *= 10
            if lib.miller_rabin_verified(num+1): hsum += num+1; print(':',num+1)
            if lib.miller_rabin_verified(num+3): hsum += num+3; print(':',num+3)
            if lib.miller_rabin_verified(num+7): hsum += num+7; print(':',num+7)
            if lib.miller_rabin_verified(num+9): hsum += num+9; print(':',num+9)
        else: num *= 10
        for d in range(10): # recursively make right trunc harshad numbers
            if num % dsum == 0: recurse(num,dsum)
            num += 1
            dsum += 1

# start recursion with 1-9 digits
for i in range(1,10): recurse(i,i)
print(hsum)
