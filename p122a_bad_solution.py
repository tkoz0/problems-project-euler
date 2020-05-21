import os,psutil

# bad solution
# 11th bfs layer needed to get m(191)
# 10 bfs layers used 9.4GB of ram and 4 minutes
# 11 bfs layer would probably need >100GB ram and 1 hour
# m(191)=11 inferred (turns out to be correct)

# begin with set {1} (only have computed x^1)
# bfs the infinite graph where you can go from {a,b,..,y} to {a,b,..,y,z} where
# z is larger than all the other elements and is the sum of 2 of them: (x^z) is
# formed by multiplying 2 elements x^a * x^b
# going strictly larger works because multiplication dependency only goes to
# smaller exponents (it is a DAG)

maxk = 200 # sum m(1)+...+m(200)
m = [0]*(maxk+1) # m(k) = m[k], m(0)=m(1)=0
#m_sol = [None]*(maxk+1) # solutions, not needed for project euler submission
#m_sol[0] = m_sol[1] = frozenset([1])


# bfs layer of sets, use frozenset (hashable) for fast repeated set checking
layer = set([frozenset([1])])
layer_num = 0 # initially 0 multiplications layer

#while None in m: # while uncomputed value exists
while layer_num < 10:
    layer2 = set() # compute next bfs layer
    for expset in layer:
        exps = sorted(expset,key=lambda x:-x) # exps[0] is largest
        for i in range(len(exps)): # larger value
            if exps[i]+exps[i] <= exps[0]: break # cant make larger value
            for j in range(i,len(exps)): # smaller value
                newexp = exps[i]+exps[j] # form larger exponent with 2 of them
                if newexp <= exps[0]: break # cant make larger value
                if newexp <= maxk: # no need to go larger than necessary
                    newset = frozenset(expset|set([newexp]))
                    layer2.add(newset)
                    # if not found yet, assign value
                    # this is minimum because BFS goes 1 step at a time in
                    # number of multiplications needed
                    if m[newexp] == 0:
                        m[newexp] = len(expset)
                        #m_sol[newexp] = newset
    print(': memory used %dMB'%
        (psutil.Process(os.getpid()).memory_info().rss>>20,))
    layer = layer2 # for next BFS iteration
    layer_num += 1
    print(': computed %d mults layer, %d sets'%(layer_num,len(layer)))
print(': bfs done')

#print(':',m)
#print(':',m_sol)
missing_values = False
for i,v in enumerate(m):
    if i > 1 and v == 0:
        print(': missing m(%d)'%i)
print(sum(m))
# have to add the missing value m(191)=11
