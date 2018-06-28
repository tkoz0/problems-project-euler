
length = 50

# count ways (including no tiles, subtract at end)
# the method is dynamic programming very similar to p114 and p115
r2ways = [1,1,2]
g3ways = [1,1,1,2]
b4ways = [1,1,1,1,2]

while len(r2ways) <= length:
    r2ways.append(r2ways[-1]) # no tile in new space
    r2ways[-1] += r2ways[-3] # a red tile in new space

while len(g3ways) <= length:
    g3ways.append(g3ways[-1])
    g3ways[-1] += g3ways[-4]

while len(b4ways) <= length:
    b4ways.append(b4ways[-1])
    b4ways[-1] += b4ways[-5]

# sum the ways that exclude having no tiles

print(': red',r2ways)
print(': green',g3ways)
print(': blue',b4ways)
print(r2ways[-1] + g3ways[-1] + b4ways[-1] - 3)
