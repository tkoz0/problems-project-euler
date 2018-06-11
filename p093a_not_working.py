import libtkoz as lib
import math

def gen_sets():
    for a in range(1,10):
        for b in range(a+1,10):
            for c in range(b+1,10):
                for d in range(c+1,10):
                    yield [a,b,c,d]
arith = ['+','-','*','/']

def eval(s): # evaluate arithmetic expression using a parse tree
    global arith
    if s[0] == '(' and s[-1] == ')': s = s[1:-1] # remove outer parenthesis
    exprs = []
    curexp = ''
    depth = 0
    for c in s:
        if depth == 0 and c in arith:
            exprs.append(curexp)
            exprs.append(c)
            curexp = ''
            continue
        if c == '(': depth += 1
        if c == ')': depth -= 1
        curexp += c
    exprs.append(curexp)
    # first do multiplication and division left to right
    found = True
    while found:
        found = False
        for i in range(len(exprs)):
            if exprs[i] == '*':
                exprs = exprs[:i-1] + [str(eval(exprs[i-1]) * eval(exprs[i+1]))] + exprs[i+2:]
                exprs[i-1] = exprs[i-1].replace('-','n') # use n for negative
                found = True
                break
            if exprs[i] == '/':
                # purposely throw off calculation if division by zero
                if math.fabs(eval(exprs[i+1])) < 0.0001:
                    exprs = exprs[:i-1] + ['4000000000'] + exprs[i+2:]
                else:
                    exprs = exprs[:i-1] + [str(eval(exprs[i-1]) / eval(exprs[i+1]))] + exprs[i+2:]
                exprs[i-1] = exprs[i-1].replace('-','n') # use n for negative
                found = True
                break
    # next addition and subtraction from left to right
    found = True
    while found:
        found = False
        for i in range(len(exprs)):
            if exprs[i] == '+':
                exprs = exprs[:i-1] + [str(eval(exprs[i-1]) + eval(exprs[i+1]))] + exprs[i+2:]
                exprs[i-1] = exprs[i-1].replace('-','n') # use n for negative
                found = True
                break
            if exprs[i] == '-':
                exprs = exprs[:i-1] + [str(eval(exprs[i-1]) - eval(exprs[i+1]))] + exprs[i+2:]
                exprs[i-1] = exprs[i-1].replace('-','n') # use n for negative
                found = True
                break
    assert len(exprs) == 1
    exprs[0] = exprs[0].replace('n','-')
    exprs = float(exprs[0])
    if math.fabs(exprs-round(exprs)) > 0.0001: return -1 # for non integers
    return round(exprs)

bestdigits = []
max1to_n = 0
for dset in gen_sets():
    dset=[3,5,7,9]
    print(dset)
    nums = set() # numbers that can be created with the expressions
    while True: # go through all permutations of the digits
        # try all possible arithmetic operations and parenthesis
        for op1 in range(4):
            for op2 in range(4):
                for op3 in range(4):
                    a,b,c,d=str(dset[0]),str(dset[1]),str(dset[2]),str(dset[3])
                    nums.add(eval(a+arith[op1]+b+arith[op2]+c+arith[op3]+d))
                    nums.add(eval('('+a+arith[op1]+b+')'+arith[op2]+c+arith[op3]+d))
                    nums.add(eval('('+a+arith[op1]+b+arith[op2]+c+')'+arith[op3]+d))
                    nums.add(eval('(('+a+arith[op1]+b+')'+arith[op2]+c+')'+arith[op3]+d))
                    nums.add(eval('('+a+arith[op1]+'('+b+arith[op2]+c+'))'+arith[op3]+d))
                    nums.add(eval(a+arith[op1]+'('+b+arith[op2]+c+')'+arith[op3]+d))
                    nums.add(eval(a+arith[op1]+'('+b+arith[op2]+c+arith[op3]+d+')'))
                    nums.add(eval(a+arith[op1]+'(('+b+arith[op2]+c+')'+arith[op3]+d+')'))
                    nums.add(eval(a+arith[op1]+'('+b+arith[op2]+'('+c+arith[op3]+d+'))'))
                    nums.add(eval(a+arith[op1]+b+arith[op2]+'('+c+arith[op3]+d+')'))
        if not lib.lexico_next(dset): break
    maxn = 1
    print(sorted(list(nums)))
    while maxn in nums: maxn += 1
    if maxn-1 > max1to_n:
        bestdigits = sorted(dset)
        max1to_n = maxn-1
print(''.join(str(d) for d in bestdigits))
