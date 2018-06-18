
nummax = 250250
divisibility = 250
modulus = 10**16 # for solution

# building sets 1 element at a time, ~20sec (cpython / i5-2540m)

setswithmod = [0] * divisibility
setswithmod[0] = 1 # empty set

for n in range(1,nummax+1):
    mod = pow(n,n,divisibility) # mod residue of next element of the set
    # for mod i sets, begin by counting the original
    # if current element is added to (i-mod)%div sets then we get mod i sets
    # so count those into the mod i sets as well
    setswithmod = list((setswithmod[(i-mod)%divisibility]+setswithmod[i])
                       % modulus for i in range(divisibility))
#    assert (sum(setswithmod) % modulus) == pow(2,n,modulus)
print((setswithmod[0]-1)%modulus) # exclude empty set
