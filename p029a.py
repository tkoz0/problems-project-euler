import math

# limits for a^b
amax = 100
bmax = 100

# use a set and insert all to it, count unique values by set size
values = set()
for a in range(2, amax+1):
    for b in range(2, bmax+1):
        values.add(math.pow(a, b))
print(len(values))

# count duplicates based on prime factorization
dupes = 0

# TODO

print(': counted', dupes, 'dupes')
print((amax-1)*(bmax-1) - dupes)

