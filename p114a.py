
length = 50

# how many ways to place blocks on different length
ways = [1,1,1,2]

while len(ways) <= length:
    curlen = len(ways)
    ways.append(ways[-1]) # if last space is empty
    # consider the first block placed and how many ways to fill the rest
    # for example, if length is L, first block is n, then we must count ways
    # to fill the L-n-1 spaces skipping the 1 space that must be empty
    for firstblock in range(3,curlen):
        ways[-1] += ways[-firstblock-2]
    ways[-1] += 1 # fill with one single block
print(':',ways)
print(ways[-1])
