
sumto = 100

# brute force recursive, extremely slow, takes ~20min (i5-2540m)

count = 0
# add numbers in decreasing order to ensure no duplicates
def recurse(total, prevnum):
    global count, sumto
    if total == sumto:
        count += 1
        return
    for i in range(1,min(prevnum+1,sumto-total+1)):
        recurse(total+i,i)
recurse(0,sumto-1) # use prevnum 99 to exclude 100 itself which "isnt a sum"
print(count)
