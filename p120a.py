
amax = 1000

# expand (a-1)^n and (a+1)^n (binomial theorem) then add
# if n even we get 2, if n odd then we get 2na
# since the modulus is a^2, we need the largest even multiple of a that is < a^2
# 2na < a^2 --> 2n < a --> pick largest even number < a

# rmax of a can be calculated as: (a-2)*a if a even else (a-1)*a

def rmax(a):
    if a % 2 == 0: return (a-2)*a
    else: return (a-1)*a

print(sum(rmax(a) for a in range(3,amax+1)))

# with summation formula, sum (a-2)*a for a = 4,6,...,1000
# and sum (a-1)*a for a = 3,5,7,...,1000
# for even a, use a=2k+2, then sum 2k*(2k+2)=4k^2+4k for k=1,2,...(amax-2)//2
# for odd a, use a=2k+1, sum 2k(2k+1)=4k^2+2k for k=1,2,...(amax-1)//2
le = (amax-2)//2 # limit for even sum
lo = (amax-1)//2 # limit for odd sum
esum = 2*(le*(le+1)*(2*le+1)//3) + 2*le*(le+1) # summation formulas
osum = 2*(lo*(lo+1)*(2*lo+1)//3) + lo*(lo+1)
print(esum+osum)

