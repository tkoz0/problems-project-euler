import libtkoz as lib
import math

data = ''
with open('data_files/p098_words.txt') as file:
    data = file.read()
data = data.split(',') # words separated by ,
data = set(w[1:-1] for w in data) # remove quotes around words
print(': read', len(data), 'words')

# convert list to unique letter sets (dict mapping sorted letters to words)
wordsets = dict()
for word in data:
    key = ''.join(sorted(word))
    if not key in wordsets: wordsets[key] = set()
    wordsets[key].add(word)
# select words that have anagrams
wordsets2 = dict()
for k in wordsets:
    if len(wordsets[k]) > 1: wordsets2[k] = wordsets[k]
wordsets = list(list(wordsets2[k]) for k in wordsets2)
# sort by length of words (larger squares will be found for larger words)
wordsets = sorted(wordsets, key = lambda x : len(x[0]), reverse = True)
print(': reduced to', sum(len(ws) for ws in wordsets), 'words')
for ws in wordsets: print(':',ws) # wordsets is a list of each wordset as a list

squares = dict()
mostdigits = 0
def gen_anagram_squares(digits):
    global squares, mostdigits
    if digits <= mostdigits: return # no need to generate more squares
    for n in range(math.ceil(math.sqrt(10**mostdigits)),
                   1+math.floor(math.sqrt(10**digits))):
        k = ''.join(sorted(str(n**2))) # insert squares into anagramic buckets
        if not k in squares: squares[k] = []
        squares[k].append(n**2)
    for k in set(squares.keys()): # remove squares that dont have an anagram
        if len(squares[k]) == 1: squares.pop(k)
    mostdigits = digits

def find_max_square(ws): # search anagramic words for largest square
    global squares
    assert len(ws) >= 2
    gen_anagram_squares(len(ws[0]))
    bestsq = (-1,-1,'','') # updated when a anagramic square is found
    for w1 in range(len(ws)): # try all word pairs
        w1i = w1 # save index for next inner loop
        w1 = ws[w1]
        for w2 in range(w1i+1,len(ws)):
            w2 = ws[w2]
            for k,v in squares.items():
                if len(k) != len(ws[0]): continue # squares must be same length
                for sq in v: # pick a square for w1
                    sqcopy = sq # save its value for use at end if needed
                    numbermap = dict() # map each letter to a digit
                    mapsuccess = True # a letter cant map to 2 different digits
                    for c in w1[::-1]:
                        if c in numbermap and sq%10 != numbermap[c]:
                            mapsuccess = False # letter cant map to 2 numbers
                            break
                        else: numbermap[c] = sq % 10
                        sq //= 10
                    # additionally require each letter to map to unique digit
                    if not mapsuccess or len(set(numbermap.values())) \
                        < len(numbermap.values()): continue
                    w2num = 0 # use the mapping to convert w2 to number
                    for c in w2: w2num = (w2num*10) + numbermap[c]
                    # found anagramic square
                    if w2num in v and max(sqcopy,w2num) > max(bestsq[:2]):
                        bestsq = (sqcopy,w2num,w1,w2)
            # pick a square for w1 and make a letter to digit mapping
            # convert w2 to a number by the mapping
            # test if this number is in the list of anagrams for that square
    return bestsq

maxsq = 0
for ws in wordsets: # assume sorted in decreasing word length
    values = find_max_square(ws)
    print(ws,find_max_square(ws))
    if max(values[:2]) > maxsq: maxsq = max(values[:2])
print(maxsq)
