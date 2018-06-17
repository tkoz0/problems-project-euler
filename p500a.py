import libtkoz as lib
import math

factorsexp = 500500
modulus = 500500507

def pgen():
    yield 2
    p = 3
    while True:
        if lib.prime(p):
            yield p
#            print(': prime',p)
        p += 2

# a bit slow, ~90 sec (cpython3 / i5-2540m)

# make a heap of primes, then to double the amount of factors, we must
# repeatedly pick the smallest exponent of a prime so that the multiplicity of
# that prime is 2^k-1 (1 less than integer exponent of 2)
# for instance, first we could pick 2 but then then next time we would have to
# pick 2^2, then 2^4, etc so the multiplicity is 1,3,7,... (2^k-1)

class heap: # binary heap to efficiently pick next primes to multiply
    def __init__(self):
        self._heap = [] # store tuples (priority,value) / (logval,val%mod)
    def _swap(self,a,b): # swap 2 elements, indexes a,b
        self._heap[a], self._heap[b] = self._heap[b], self._heap[a]
    def push(self,p,v): # push back, sift up
        i = len(self._heap)
        self._heap.append((p,v))
        while i != 0 and self._heap[(i-1)//2][0] > self._heap[i][0]:
            self._swap(i,(i-1)//2)
            i = (i-1)//2
    # return next value to multiply, then squares it and sift down
    def next_multiply(self):
        global modulus
        result = self._heap[0][1]
        self._heap[0] = (self._heap[0][0]*2.0, (self._heap[0][1]**2) % modulus)
        i = 0
        while 2*i+1 < len(self._heap): # has left child
            s = i # swap index
            if self._heap[2*i+1][0] < self._heap[s][0]: s = 2*i+1
            # has right child and is smaller
            if 2*i+2 < len(self._heap) and \
                self._heap[2*i+2][0] < self._heap[s][0]: s = 2*i+2
            if s != i:
                self._swap(i,s)
                i = s
            else: break # valid position
        return result

# store log values of primes so theyre smaller for comparing and we can store
# the actual values % modulus for efficient multiplying
# use a binary min heap to efficiently pick next amount to multiply by
pq = heap() # prime queue

numpicked = 0
result = 1

for p in pgen(): # prime generator
    if numpicked == factorsexp: break # done
    pq.push(math.log(p),p) # insert into heap
    while True:
        nextmultiply = pq.next_multiply()
        numpicked += 1
        result = (result * nextmultiply) % modulus
        if numpicked == factorsexp: break
        if nextmultiply == p: break # squared last prime, must generate another
print(result)
