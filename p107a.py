import heapq

data = ''
with open('data_files/p107_network.txt') as file:
    data = file.read()
data = list(list((None if d == '-' else int(d)) for d in line.split(','))
            for line in data.splitlines())
# some checks
for r in data: assert len(r) == len(data[0]) # rows same length
assert len(data) == len(r) # is square matrix
# diagonals empty (a vertex cant be connected to itself)
for r in range(len(data)): assert data[r][r] is None

# use a greedy algorithm to continually remove the highest weight non cut edge
# repeatedly until no more can be removed without disconnecting the graph

totalweight = 0
edgecount = 0
for r in range(len(data)):
    for c in range(r+1,len(data)):
        assert data[r][c] == data[c][r]
        if not (data[r][c] is None):
            totalweight += data[r][c]
            edgecount += 1
print(': initial total graph weigth is',totalweight)
print(': initial graph has edgecount',edgecount)

def connected(adj): # determines if graph is connected
    vertices = set()
    stack = [0]
    while len(stack) != 0:
        v = stack.pop()
        if not (v in vertices): # if this is a new vertex
            vertices.add(v)
            for u in range(len(adj)): # push adjacent vertices to stack
                if not (adj[v][u] is None): stack.append(u)
    return len(vertices) == len(adj) # could reach every vertex
print(': initial graph is connected:',connected(data))

# attempt a greedy algorithm: remove highest weight non cut edge until every
# edge is a cut edge, use a priority queue for selecting edges
pq = []
for r in range(len(data)):
    for c in range(r+1,len(data)):
        w = data[r][c]
        if w is None: continue
        pq.append((w,r,c))
heapq._heapify_max(pq)

while len(pq) != 0: # try removing edges starting from longest
    w, r, c = heapq._heappop_max(pq)
    # try removing edge
    data[r][c] = data[c][r] = None
    if not connected(data): # put edge back (it was a cut edge)
        data[r][c] = data[c][r] = w

finalweight = 0
edgecount = 0
for r in range(len(data)):
    for c in range(r+1,len(data)):
        if not (data[r][c] is None):
            finalweight += data[r][c]
            edgecount += 1

print(': final total graph weight is',finalweight)
print(': final graph has edgecount',edgecount)
print(': final graph is connected',connected(data))
print(totalweight-finalweight)
