import math

data = ''
with open('data_files/p099_base_exp.txt') as file:
    data = file.read()
# convert to list of tuples of base,exp pair
data = list(tuple(int(i) for i in d.split(',')) for d in data.splitlines())

maxln = 0 # compute max based on natural log: ln(b^e) = e*ln(b)
bestline = 0
linenum = 1
for b,e in data:
    lnval = e*math.log(b)
    if lnval > maxln:
        maxln = lnval
        bestline = linenum
    linenum += 1
print(bestline)
