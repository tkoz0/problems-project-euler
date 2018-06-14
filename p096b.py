
data = ''
with open('data_files/p096_sudoku.txt') as file:
    data = file.read()
data = data.splitlines()
assert len(data) % 10 == 0 # 10 lines / puzzle (header + 9 lines of numbers)
puzzles = []
for p in range(len(data)//10):
    puzzles.append([])
    puz = puzzles[-1]
    for l in range(p*10+1,(p+1)*10): # convert lines to integers
        puz.append(list(int(n) for n in data[l]))
print(': read', len(data)//10, 'puzzles')

# combine logic with backtracking

def in_row(p,r,n):
    return n in p[r]
def in_col(p,c,n):
    for r in range(9):
        if p[r][c] == n: return True
    return False
def in_box(p,r,c,n):
    for rr in range(3*r,3*r+3):
        for cc in range(3*c,3*c+3):
            if p[rr][cc] == n: return True
    return False

# solve with typical logic, return (contradiction boolean, list of changes)
def force_numbers(p):
    changes = []
    changed = True
    while changed: # loop until puzzle doesnt change
        changed = False
        for r in range(9): # find numbers forced into rows
            for n in range(1,10): # try each number not in the row
                if in_row(p,r,n): continue
                cols = [] # possible spaces for n
                for bc in range(3): # find boxes that number isnt in
                    if in_box(p,r//3,bc,n): continue
                    for c in range(3*bc,3*bc+3): # try spaces in this box
                        if p[r][c] != 0: continue # not empty
                        if in_col(p,c,n): continue # not valid column for n
                        cols.append(c)
                if len(cols) == 0: return (False,changes) # cant solve
                if len(cols) == 1:
                    p[r][cols[0]] = n # successful placement
                    changes.append((r,cols[0],n))
                    changed = True
        for c in range(9): # find numbers forced into columns
            for n in range(1,10):
                if in_col(p,c,n): continue
                rows = []
                for br in range(3): # find rows where n can be placed it the column
                    if in_box(p,br,c//3,n): continue
                    for r in range(3*br,3*br+3):
                        if p[r][c] != 0: continue
                        if in_row(p,r,n): continue
                        rows.append(r)
                if len(rows) == 0: return (False,changes) # unsolvable
                if len(rows) == 1:
                    p[rows[0]][c] = n # only 1 space for n
                    changes.append((rows[0],c,n))
                    changed = True
        for br in range(3): # find numbers forced into boxes
            for bc in range(3):
                for n in range(1,10):
                    if in_box(p,br,bc,n): continue
                    locs = [] # box coordinates where n can be placed
                    for r in range(3*br,3*br+3):
                        for c in range(3*bc,3*bc+3):
                            if p[r][c] != 0: continue
                            if in_row(p,r,n) or in_col(p,c,n): continue
                            locs.append((r,c))
                    if len(locs) == 0: return (False,changes)
                    if len(locs) == 1:
                        p[locs[0][0]][locs[0][1]] = n
                        changes.append((locs[0][0],locs[0][1],n))
                        changed = True
    # solved if no zeroes, return changes to board
    return (True,changes) # true means no contradiction was found

############ NEED TO CHECK / REDO (BEGIN) ############False

def place_num(p,m,r,c,n): # places number and updates markup
    assert m[r][c] == set([n])
    p[r][c] = n
    for rr in range(9): # update markup in cells than cannot have n
        if n in m[rr][c]: m[rr][c].remove(n)
    for cc in range(9):
        if n in m[r][cc]: m[r][cc].remove(n)
    br, bc = r//3, c//3
    for rr in range(3*br,3*br+3):
        for cc in range(3*bc,3*bc+3):
            if n in m[rr][cc]: m[rr][cc].remove(n)

def preemptive_sets(p): # solve with crook's algorithm (preemptive set method)
    m = list(list(set() for c in range(9)) for r in range(9)) # generate markup
    rempty, cempty = [0]*9, [0]*9 # number empty in each row and column
    bempty = list([0,0,0] for i in range(3)) # number empty in each box
    for r in range(9):
        for c in range(9):
            if p[r][c] != 0: continue # no preemptive set for nonempty cells
            rempty[r] += 1
            cempty[c] += 1
            bempty[r//3][c//3] += 1
            for n in range(1,10): # find possible placement numbers
                if in_row(p,r,n) or in_col(p,c,n) or in_box(p,r//3,c//3,n):
                    continue
                m[r][c].add(n)
    ######## FIX BELOW ########
    changes = []
    changed = True
    while changed:
        changed = False
        for r in range(9): # place numbers from preemptive set size 1
            for c in range(9):
                if p[r][c] != 0: continue
                if len(m[r][c]) == 0: return False # cant solve
        for r in range(9): # try sets for each row
            pass
        for c in range(9): # try sets for each column
            pass
        for br in range(3): # try sets for each box
            for bc in range(3):
                pass
    return set((0 in r) for r in p) == set([False]) # solved if no zeroes

############ NEED TO CHECK / REDO (END) ###############

def filled(p):
    return set((0 in r) for r in p) == set([False]) # no zeroes

def count_zeroes(p):
    return sum(sum(1 for c in r if c == 0) for r in p)

def solve(p,depth): # use logic, make guesses on recursive search paths if needed
    result1 = force_numbers(p)
    if filled(p): return True # solved
    if result1[0] is True: # successful in logic progress, guess recursively
        done = False
        for r in range(9):
            if done: break
            for c in range(9): # find empty cell
                if p[r][c] != 0: continue
                nums = [True]*10 # find possible numbers (true)
                for rr in range(9): nums[p[rr][c]] = False
                for cc in range(9): nums[p[r][cc]] = False
                for rr in range(3*(r//3),3*(r//3)+3):
                    for cc in range(3*(c//3),3*(c//3)+3):
                        nums[p[rr][cc]] = False
                for n in range(1,10): # try each possible number
                    if not nums[n]: continue
                    p[r][c] = n
                    if solve(p,depth+1): return True
                p[r][c] = 0 # backtrack (none of these search paths worked)
                done = True
                break # no valid guess makes valid solution, unsolvable
    # undo changes (backtrack) (if guessing fails or logic found contradiction)
    for change in result1[1]: p[change[0]][change[1]] = 0 # reset changed cells
    return False # unable to find solution path starting from here

total = 0
for i,p in enumerate(puzzles):
    print(': puzzle',i+1,solve(p,0))
    total += 100*p[0][0]+10*p[0][1]+p[0][2]
print(total)
