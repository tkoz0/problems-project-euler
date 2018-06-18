
nummax = 250250
divisibility = 250
modulus = 10**16 # for solution

# building sets 1 element at a time, ~40sec (cpython / i5-2540m)

setswithmod = [0] * divisibility
setswithmod[0] = 1 # empty set

for n in range(1,nummax+1):
    mod = pow(n,n,divisibility) # mod residue of next element of the set
    swmtmp = setswithmod[:] # amount for each existing subset
    # for each existing subset, add mod to it and count it
    for m in range(divisibility):
        swmtmp[(m+mod)%divisibility] += setswithmod[m]
        swmtmp[(m+mod)%divisibility] %= modulus
    setswithmod = swmtmp
#    assert (sum(setswithmod) % modulus) == pow(2,n,modulus)
print((setswithmod[0]-1)%modulus) # exclude empty set
