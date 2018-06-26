import libtkoz as lib

Sn = 4

# basic brute force approach, recursively generates all 10 digits numbers and
# considers the primes

dcounts = [0]*10 # instances of each digit
digits = []
# index with [digit][num repeated], store counts and sums respectively
drepcount = list(list(0 for i in range(Sn)) for j in range(10))
drepsum = list(list(0 for i in range(Sn)) for j in range(10))
def recurse():
    global Sn, dcounts, digits, drepcount, drepsum
    if len(digits) == Sn: # 10 digit number to include
        n = 0
        for d in digits: n = (10*n) + d # make number
        if lib.prime(n): # if prime, consider in counting and summing
            for d,c in enumerate(dcounts):
                drepcount[d][c] += 1
                drepsum[d][c] += n
    else:
        digits.append(0)
        for d in range(10):
            dcounts[d] += 1
            digits[-1] = d
            recurse() # try with next digit
            dcounts[d] -= 1 # backtrack
        digits.pop() # backtrack
digits.append(0)
for d in range(1,10): # initialize recursion with starting digits
    print(': recursing starting digit',d)
    dcounts[d] += 1
    digits[-1] = d
    recurse()
    dcounts[d] -= 1 # backtrack

total = 0 # result
for d in range(10): # consider all digits
    for c in range(Sn-1,-1,-1):
        if drepcount[d][c] != 0:
            print(': M(',Sn,',',d,') = ',c)#,sep='')
            print(': N(',Sn,',',d,') = ',drepcount[d][c])#,sep='')
            print(': S(',Sn,',',d,') = ',drepsum[d][c])#,sep='')
            total += drepsum[d][c]
            break
print(total)
