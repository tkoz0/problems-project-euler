
arith = {'+': lambda x, y: x + y,
         '-': lambda x, y: x - y,
         '*': lambda x, y: x * y,
         '/': lambda x, y: x / y}

def gen_sets():
    for a in range(1,10):
        for b in range(a+1,10):
            for c in range(b+1,10):
                for d in range(c+1,10):
                    yield [a,b,c,d]

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
