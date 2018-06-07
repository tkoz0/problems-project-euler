
divby = 1000000

# takes ~8sec (i5-2540m)
# use the relationship to the pentagonal number theorem
# p(n) = p(n-1) + p(n-2) - p(n-5) - p(n-7) + ...
# the constants 1,2,5,7,... are nonzero generalized pentagonal numbers
# evaluate for generalized pentagonal numbers up to n
# pentagonal numbers g: order g_1, g_-1, g_2, g_-2, ...
# this sequence is increasing (provable by induction with cases)

def pent_gen(): # pentagonal constants generator
    pent = lambda k : k * (3*k - 1) // 2
    i = 1
    neg = False # alternate signs, use positive part but sign means add/subtract
    while True: # yield next 2 (consecutive same sign pairs)
        if neg:
            yield -pent(i)
            yield -pent(-i)
        else:
            yield pent(i)
            yield pent(-i)
        neg = not neg
        i += 1

pentgen = pent_gen()
pentlist = [next(pentgen)] # begin with 1st in sequence
ways = [1]
coins = 1
while True:
    # generate next pentagonal number if coins exceeds whats in the list
    if coins > pentlist[-1]: pentlist.append(next(pentgen))
    ways.append(0) # start 0, sum based on pentagonal numbers
    for pent in pentlist:
        if abs(pent) > coins: break # cant exceed limit
        if pent > 0: # add value
            ways[coins] += ways[coins - pent]
        else: # subtract value
            ways[coins] -= ways[coins + pent]
        ways[coins] %= divby
    if ways[coins] == 0: break # divisible by required number
    coins += 1
print(coins)
