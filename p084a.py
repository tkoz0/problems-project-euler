import random

random.seed(42) # for consistent results
steps = 1000000 # how many steps to run the simulation for
# board cycle, property sets are a,b,c,d,e,f,g,h, g2j=go2jail
# cc=com chest, t=tax, r=railroad, ch=chance, u=utility, fp=free park
board = ['GO', 'A1', 'CC1', 'A2', 'T1', 'R1', 'B1', 'CH1', 'B2', 'B3',
         'JAIL', 'C1', 'U1', 'C2', 'C3', 'R2', 'D1', 'CC2', 'D2', 'D3',
         'FP', 'E1', 'CH2', 'E2', 'E3', 'R3', 'F1', 'F2', 'U2', 'F3',
         'G2J', 'G1', 'G2', 'CC3', 'G3', 'R4', 'CH3', 'H1', 'T2', 'H2']
dicemax = 4

positions = dict() # map board positions to index in list
for i,pos in enumerate(board): positions[pos] = i

def roll_dice(): # returns tuple of 2 dice
    global dicemax
    return (1+random.randrange(dicemax),1+random.randrange(dicemax))

# approximate the solution with a monte carlo simulation

print(': running simulation with', steps, 'turns')
counts = [0] * len(board) # times visiting each position
position = 0 # start at go
doubles = 0
chance = 0 # index of chance card
commchest = 0 # index of community chest card
for turn in range(steps):
    dice = roll_dice()
    if dice[0] == dice[1]: doubles += 1 # rolled double
    else: doubles = 0
    position = (position + sum(dice)) % len(board)
    # deal with all possible additional movements
    if doubles == 3 or board[position] == 'G2J': # go directly to jail
        position = positions['JAIL']
        doubles = 0 # reset rolls
    elif board[position].startswith('CC'): # community chest may move player
        commchest += 1
        cc = commchest % 16 # 16 cards in deck
        # 2 cards cause player to move
        if cc == 0: position = positions['GO']
        elif cc == 1: position = positions['JAIL']
    elif board[position].startswith('CH'): # chance may move player
        chance += 1
        ch = chance % 16 # 16 cards in deck
        # 10 cards cause player to move
        if ch == 0: position = positions['GO']
        elif ch == 1: position = positions['JAIL']
        elif ch == 2: position = positions['C1']
        elif ch == 3: position = positions['E3']
        elif ch == 4: position = positions['H2']
        elif ch == 5: position = positions['R1']
        elif ch == 6 or cc == 7: # next R
            while True:
                position = (position+1) % len(board)
                if board[position].startswith('R'): break
        elif ch == 8: # next U
            while True:
                position = (position+1) % len(board)
                if board[position].startswith('U'): break
        elif ch == 9: position = (position-3) % len(board)
    counts[position] += 1 # finish visiting at this position
assert counts[positions['G2J']] == 0 # should never finish on go to jail
print(': drew', chance, 'chance cards and', commchest, 'commchest cards')

# compute probabilities
probs = []
for i,c in enumerate(counts): probs.append((c/steps,board[i]))
probs.sort()
print(':', probs)

# construct 6 digit string
likely = [positions[probs[-1][1]], positions[probs[-2][1]],
          positions[probs[-3][1]]]
print(format(likely[0],'02d'), format(likely[1],'02d'),
      format(likely[2],'02d'), sep='')
