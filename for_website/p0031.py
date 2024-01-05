P = 200
c = [1,2,5,10,20,50,100,200]

W = [[0]*(P+1) for _ in range(len(c))]

# i is 1 indexed in explanation but 0 indexed here
for i in range(len(c)):
    for p in range(P+1):
        if p == 0:
            W[i][p] = 1
        elif p < c[i] and i > 0:
            W[i][p] = W[i-1][p]
        else: # p >= c[i]
            W[i][p] = W[i][p-c[i]]
            if i > 0:
                W[i][p] += W[i-1][p]
print(W[-1][P])

W = [0]*(P+1)
W[0] = 1
for ci in c:
    for p in range(ci,P+1):
        W[p] += W[p-ci]
print(W[P])
