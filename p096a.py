
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

def backtrack(p, i):
    if i == 9*9: return True # successfully filled whole puzzle
    r, c = i//9, i%9
    if p[r][c] != 0: return backtrack(p,i+1) # try next cell
    digits = [True] * 10 # cross out numbers that cant be placed here
    for jr in range(9): digits[p[jr][c]] = False # row
    for jc in range(9): digits[p[r][jc]] = False # column
    sr, sc = r//3, c//3
    for jr in range(3*sr,3*(sr+1)): # sub block
        for jc in range(3*sc,3*(sc+1)):
            digits[p[jr][jc]] = False
    for j in range(1,10): # try each number recursively
        if not digits[j]: continue # cant place this one
        p[r][c] = j
        if backtrack(p,i+1): return True
    p[r][c] = 0 # backtrack
    return False

# solve every puzzle with simple backtracking, ~8 sec (i5-2540m)
for i,p in enumerate(puzzles):
    assert backtrack(p, 0), 'couldnt solve puzzle {0:d}'.format(i+1)
    print(': solved puzzle',i+1)
print(sum(100*p[0][0]+10*p[0][1]+p[0][2] for p in puzzles))
