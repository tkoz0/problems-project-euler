
data = ''
with open('data_files/p099_base_exp.txt') as file:
    data = file.read()
# convert to list of tuples of base,exp pair
data = list(tuple(int(i) for i in d.split(',')) for d in data.splitlines())

# slower solution using python big integer capabilities, ~30min (i5-2540m)

maxval = 0
bestline = 0
linenum = 1
for b,e in data:
    print(': line =',linenum)
    val = b**e
    if val > maxval:
        maxval = val
        bestline = linenum
    linenum += 1
print(bestline)
