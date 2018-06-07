
divby = 1000000

# dynamic programming approach, though n^2 it scales poorly, solution is large
# takes ~15min (i5-2540m)

maxcoins = 32
while True:
    print(': trying maxcoins =', maxcoins)
    ways = [0] * (maxcoins+1)
    ways[0] = 1
    for pile1 in range(1,maxcoins):
        for i in range(pile1,maxcoins+1):
            ways[i] += ways[i-pile1]
    # find a coin set size that is a multiple of the required number
    solution = -1
    for i,w in enumerate(ways):
        if w % divby == 0:
            solution = i
            break
    if solution != -1:
        print(': coin set size', solution, 'can be partitioned in',
              ways[solution], 'ways')
        print(solution)
        break
    maxcoins *= 2
