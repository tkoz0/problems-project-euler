
# represent state as array of integer 0-15
# bits a,b,c,d for y=3,y=2,y=1,y=0
def all_divides(start):
    for x in range(len(start)):
        # use before to find amoeba, after is whree it splits to
        for before,after in [(1,3),(2,6),(4,12),(8,9)]:
            if (start[x] & before) == 0:
                continue # no amoeba
            if (start[x+1] & after) != 0:
                continue # amoeba in 1 of the target squares
            yield start[:x]+(start[x]-before,start[x+1]|after)+start[x+2:]

#print(list(all_divides((0,1,4,6,0,0))))
#quit()

# assumes at least 1 nonzero column (always true in this problem)
def largest_column(state):
    i = len(state)-1
    while state[i] == 0:
        i -= 1
    return i

DEPTH = 20

# DP[amoeba divisions][largest column]
DP = [[0]*(DEPTH+1) for _ in range(DEPTH+1)]
layer = {(1,)+(0,)*DEPTH:None}
print('C(0)=1')
print(layer)
DP[0][0] = 1

for d in range(DEPTH):
    print()
    print(f'computing layer {d+1}')
    layer2 = dict() # state to its previous
    dups = 0
    for state in layer:
        #print(f'    alldivides({state})={list(all_divides(state))},dup={len(list(all_divides(state)))!=len(set(all_divides(state)))}')
        for newstate in all_divides(state):
            if newstate in layer2:
                dups += 1
                #print(f'    dup {newstate} from {state}')
            else:
                layer2[newstate] = state
    layer = layer2
    print(f'C({d+1})={len(layer)}')
    #print(f'    dups={dups}')
    #print(layer)
    # update DP table
    for state in layer:
        DP[d+1][largest_column(state)] += 1

# print DP table
WIDTH = 8
assert WIDTH >= 5
print()
print(' '*(WIDTH-1)+'A' + ''.join(f'%{WIDTH}d'%i for i in range(DEPTH+1)) + ' '*(WIDTH-4) + 'C(A)')
for a in range(DEPTH+1):
    print(f'%{WIDTH}d'%a + ''.join(f'%{WIDTH}d'%v for v in DP[a]) + f'%{WIDTH}d'%sum(DP[a]))
