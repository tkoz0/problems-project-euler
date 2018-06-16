
sumto = 0.5
maxn = 45
epsilon = 1/(2**45) # should be sufficiently small for this problem

# generate sum of 1/n^2 + 1/(n+1)^2 + ... + 1/maxn^2 for faster performance
cumulativesum = ([0.0] * maxn) + [1/(maxn**2)]
for i in range(maxn-1,1,-1):
    cumulativesum[i] = cumulativesum[i+1] + 1/(i**2)
print(': cumulative sums', cumulativesum)

count = 0
def recurse(s,n):#,sqs):
    global sumto, maxn, count, epsilon, cumulativesum
    if n > maxn: return
    if sumto - (s + cumulativesum[n]) > epsilon:
        return # too much distance to reach sum
    if abs(s-sumto) < epsilon: # cose enonugh to required sum
        count += 1
#        print(sqs,sum(1/x**2 for x in sqs))
        return
    recurse(s,n+1)#,sqs) # try each recursively
    s += 1/(n**2)
    if s <= sumto + epsilon: recurse(s,n+1)#,sqs+[n])

recurse(0,2)#,[])
print(count)
