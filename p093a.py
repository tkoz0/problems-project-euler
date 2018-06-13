import libtkoz as lib

arith = {'+': lambda x, y: x + y,
         '-': lambda x, y: x - y,
         '*': lambda x, y: x * y,
         '/': lambda x, y: x / y}

def gen_sets():
    for a in range(1,10):
        for b in range(a+1,10):
            for c in range(b+1,10):
                for d in range(c+1,10):
                    yield [str(a),str(b),str(c),str(d)]

def float_near(a, b): return abs(a-b) < 0.0001

# evaluate arithmetic expression, parse tree method
# returns false if the expression is invalid
def eval(expr):
    if type(expr) is float: return expr
    global arith
    # divide the expression string by the arithmetic operators
    exprsplit = []
    exprcurrent = ''
    exprdepth = 0
    for c in expr:
        if c == '(': exprdepth += 1
        elif c == ')': exprdepth -= 1
        elif exprdepth == 0 and c in arith:
            exprsplit.append(exprcurrent)
            exprsplit.append(c) # operation
            exprcurrent = ''
            continue
        if exprdepth < 0: return False
        exprcurrent += c
    if exprdepth != 0: return False
    exprsplit.append(exprcurrent)
    # remove outer parenthesis and evaluate
    if len(exprsplit) == 1 and exprsplit[0][0] == '(' \
        and exprsplit[0][-1] == ')':
        return eval(exprsplit[0][1:-1])
    # evaluate * and / from left to right (order of operations)
    i = 1
    while i < len(exprsplit)-1:
        if exprsplit[i] in ['*', '/']:
            left = eval(exprsplit[i-1])
            right = eval(exprsplit[i+1])
            if (left is False) or (right is False): return False
            if exprsplit[i] == '/' and float_near(right, 0):
                return False # division by 0 occurs
            exprsplit = exprsplit[:i-1] + \
                        [arith[exprsplit[i]](left, right)] \
                        + exprsplit[i+2:]
        else: i += 2 # try next operator
    # evaluate + and - from left to right (order of operations)
    i = 1
    while i < len(exprsplit)-1:
        if exprsplit[i] in ['+', '-']:
            left = eval(exprsplit[i-1])
            right = eval(exprsplit[i+1])
            if (left is False) or (right is False): return False
            exprsplit = exprsplit[:i-1] + \
                        [arith[exprsplit[i]](left, right)] \
                        + exprsplit[i+2:]
        else: i += 2 # try next operator
    if len(exprsplit) != 1: return False
    return float(exprsplit[0])

def make_expr(*args):
    s = ''
    for arg in args:
        if type(arg) is str: s += arg
        if type(arg) is int: s += ['+','-','*','/'][arg]
    return s

bestdigits = []
max1to_n = 0
arithexprs = list(arith.keys())
for dset in gen_sets():
    nums = set() # numbers that can be created with the expressions
    while True: # go through all permutations of the digits
        # try all possible arithmetic operations and parenthesis
        for op1 in range(4):
            for op2 in range(4):
                for op3 in range(4):
                    a,b,c,d=dset[0],dset[1],dset[2],dset[3]
                    nums.add(eval(a+arithexprs[op1]+b+arithexprs[op2]+c+arithexprs[op3]+d))
                    nums.add(eval('('+a+arithexprs[op1]+b+')'+arithexprs[op2]+c+arithexprs[op3]+d))
                    nums.add(eval('('+a+arithexprs[op1]+b+arithexprs[op2]+c+')'+arithexprs[op3]+d))
                    nums.add(eval('(('+a+arithexprs[op1]+b+')'+arithexprs[op2]+c+')'+arithexprs[op3]+d))
                    nums.add(eval('('+a+arithexprs[op1]+'('+b+arithexprs[op2]+c+'))'+arithexprs[op3]+d))
                    nums.add(eval(a+arithexprs[op1]+'('+b+arithexprs[op2]+c+')'+arithexprs[op3]+d))
                    nums.add(eval(a+arithexprs[op1]+'('+b+arithexprs[op2]+c+arithexprs[op3]+d+')'))
                    nums.add(eval(a+arithexprs[op1]+'(('+b+arithexprs[op2]+c+')'+arithexprs[op3]+d+')'))
                    nums.add(eval(a+arithexprs[op1]+'('+b+arithexprs[op2]+'('+c+arithexprs[op3]+d+'))'))
                    nums.add(eval(a+arithexprs[op1]+b+arithexprs[op2]+'('+c+arithexprs[op3]+d+')'))
        if not lib.lexico_next(dset): break
    nums2 = set() # use integer values for everything
    for n in nums:
        if float_near(n, round(n)): nums2.add(round(n))
    nums = nums2
    maxn = 1
    while maxn in nums: maxn += 1
    print(':', sorted(dset), maxn-1)
    if maxn-1 > max1to_n:
        bestdigits = sorted(dset)
        max1to_n = maxn-1
print(': max 1 to n in set:', max1to_n)
print(''.join(str(d) for d in bestdigits))
