
card = { '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
         'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14 }

# determine hand type, assumes it is sorted
# returns number to identify what to break a tie, 0 if not that type

def is_one_pair(h):
    for i in range(1,5):
        if h[i-1][0] == h[i][0]: return h[i][0]
    return 0

# tie breaking metric = 100*higher + lower, compare higher first
def is_two_pairs(h):
    for i in range(1,5):
        for j in range(i+2,5):
            if h[i-1][0] == h[i][0] and h[j-1][0] == h[j][0]:
                hi = max(h[i][0], h[j][0])
                lo = min(h[i][0], h[j][0])
                return 100*hi+lo
    return 0

def is_three_of_a_kind(h):
    for i in range(2,5):
        if h[i-2][0] == h[i-1][0] == h[i][0]: return h[i][0]
    return 0

def is_straight(h): # use highest card
    for i in range(1,5):
        if h[i][0] != h[0][0] + i: return 0 # in sequence
    return h[-1][0]

def is_flush(h): # use highest card
    for i in range(1,5):
        if h[i][1] != h[0][1]: return 0 # same suite
    return h[-1][0]

# tie breaker metric: 100*(3set)+(2set)
def is_full_house(h):
    if (h[0][0] == h[1][0] and h[2][0] == h[3][0] == h[4][0]):
        return 100*h[2][0]+h[1][0]
    if (h[0][0] == h[1][0] == h[2][0] and h[3][0] == h[4][0]):
        return 100*h[2][0]+h[3][0]
    return 0

def is_four_of_a_kind(h):
    for i in range(3,5):
        if h[i-3][0] == h[i-2][0] == h[i-1][0] == h[i][0]: return h[i][0]
    return 0

def is_straight_flush(h):
    if is_flush(h) and is_straight(h): return h[-1][0]
    return 0

def is_royal_flush(h): # no tie breaker metric, just use 1
    if h[0][0] == 10 and is_straight_flush(h): return 1
    return 0

# in order starting with most specific / best to least specific / worst
handtypes = [is_royal_flush, is_straight_flush, is_four_of_a_kind,
             is_full_house, is_flush, is_straight, is_three_of_a_kind,
             is_two_pairs, is_one_pair]
# for debugging
funcnames = ['is_royal_flush', 'is_straight_flush', 'is_four_of_a_kind',
             'is_full_house', 'is_flush', 'is_straight', 'is_three_of_a_kind',
             'is_two_pairs', 'is_one_pair', 'is_junk']

# cards will be tuples (value, suite) as (int, char)
# hands will be list of 5 cards
# 1 game will be a tuple of 2 hands

data = ''
with open('data_files/p054_poker.txt') as file:
    data = file.read()
data = data.splitlines()
for i,l in enumerate(data):
    data[i] = l.split(' ')
    for j,c in enumerate(data[i]):
        data[i][j] = (card[data[i][j][0]], data[i][j][1])
    data[i] = (sorted(data[i][:5]), sorted(data[i][5:]))

wins, losses, draws = 0, 0, 0 # in terms of player 1 (index 0 in game)
for game in data:
    p1, p2 = -1, -1 # -1 until hand type determined
    p1m, p2m = -1, -1 # tie breaker metric
    for i,t in enumerate(handtypes): # use function to find hand type
        if p1 == -1 and t(game[0]) != 0: p1, p1m = i, t(game[0])
        if p2 == -1 and t(game[1]) != 0: p2, p2m = i, t(game[1])
    # hand type is junk, use highest card, set p1,p2 to high numbers for worst
    if p1 == -1: p1, p1m = len(handtypes), game[0][-1][0]
    if p2 == -1: p2, p2m = len(handtypes), game[1][-1][0]
    # lower number means better hand type (p1, p2)
    # p1m and p2m are the tie breaker metric, higher is better
    if p1 < p2: wins += 1 # compare hand type
    elif p1 > p2: losses += 1
    elif p1m > p2m: wins += 1 # same hand type, use tie breaker metric
    elif p1m < p2m: losses += 1
    else: draws += 1 # draw
#    print(game[0], funcnames[p1], p1m)
#    print(game[1], funcnames[p2], p2m)
#    if p1==p2 and p1m==p2m: print('. draw')
#    else: print('.', 'win' if (p1<p2 or (p1==p2 and p1m>p2m)) else 'loss')
print(': wins', wins)
print(': losses', losses)
print(': draws', draws)
print(wins)
