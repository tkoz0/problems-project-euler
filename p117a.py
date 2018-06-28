
length = 50

# this method is very similar to p114, p115, and p116

ways = [1]

while len(ways) <= length:
    ways.append(ways[-1]) # no tile in new space
    if len(ways) > 2: ways[-1] += ways[-3] # red(2) tile
    if len(ways) > 3: ways[-1] += ways[-4] # green(3) tile
    if len(ways) > 4: ways[-1] += ways[-5] # blue(4) tile

print(ways[-1])
