
data = ''
with open('data_files/p079_keylog.txt') as file:
    data = file.read()
data = set(data.splitlines()) # keep as chars, remuve duplicates
print(': logons', data)
charset = set()
for logon in data: # make a set of used passcode chars
    for c in logon:
        charset.add(c)
print(': charset', charset)

# find what comes before each char
before = dict()
for c in charset: before[c] = set()
for logon in data:
    for i,c in enumerate(logon):
        for cc in logon[:i]: before[c].add(cc)
print(': before each char')
for c in before: print(':  ', c, before[c])

# now build the solution, start with what has nothing before it
# then remove that from all the sets and find the next empty set and so on
# this could be done by creating the solution in order sorted by the size
# of the set of how many digits are before it
solution = [''] * len(charset)
for s in before: # use set length as index in solution
    solution[len(before[s])] = s

# if any numbers need to be duplicated, just duplicate them
maxcounts = dict()
for c in charset: maxcounts[c] = 0
for logon in data:
    for c in charset:
        maxcounts[c] = max(maxcounts[c], logon.count(c))
print(': maximum count of each char', maxcounts)

# build solution with order and maximum count of each character
solutionstr = ''
for c in solution:
    solutionstr += c * maxcounts[c]
print(solutionstr)
