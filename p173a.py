import math

tiles = 10**6

outerside = 1
count = 0
while True:
    # find the smallest number (innerside) with same parity as outerside such
    # that outerside**2 - innerside**2 <= 1000000 --> out**2 - 1000000 <= in**2
    # innerside = ceil(sqrt(out**2 - 1000000))
    # if out**2-1000000<0 then count all lamina with this outer side length
    if outerside**2 - tiles <= 0:
        # include 1,3,...,n-2 or 2,4,...,n-2 for inner radius: (outer-1)//2
        count += (outerside-1)//2
    else: # compute minimum inner side length
        innerside = math.ceil(math.sqrt(outerside**2 - tiles))
        if innerside % 2 != outerside % 2: innerside += 1 # have same parity
        if innerside >= outerside: break # no lamina
        # count inner,inner+2,...,outer-2 = (outer-inner)//2
        count += (outerside-innerside)//2
    outerside += 1
print(count)
