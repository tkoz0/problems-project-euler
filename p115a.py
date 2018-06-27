
m = 50
exceedways = 10**6

# very similar to p114 solution, reusing code and concepts, see p114 for details

# len < m --> cant place m length block, len = m --> m length block or none
ways = ([1]*m) + [2]

while ways[-1] <= exceedways:
    curlen = len(ways)
    ways.append(ways[-1])
    for firstblock in range(m,curlen):
        ways[-1] += ways[-firstblock-2]
    ways[-1] += 1
print(':',ways)
print(len(ways)-1) # index of last element is length
