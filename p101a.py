from fractions import Fraction

gen_poly = list((-1)**i for i in range(10+1))

# polynomials are lists: a_0, a_1, ... representing a_0+a_1*x+a_2*x^2+...

def eval(poly,n): # evaluates a polynomial at n
    x = 1 # n^i for i=0 to highest exponent
    val = 0
    for coeff in poly:
        val += coeff * x
        x *= n
    return val

gen_terms = list(eval(gen_poly,n) for n in range(len(gen_poly)))
print(': generating polynomial coeffs',gen_poly)
print(': generating polynomial values',gen_terms)

# notation: g(n) is the generating polynomial, p(n) is an approximation
# to approximate k values OP(k,n), approximate with a k-1 degree polynomial
# for example with k=3, solve the linear system for a degree 2 approximation
# 1 1 1 g(1)
# 1 2 4 g(2)
# 1 3 9 g(3) (the solution x_0,x_1,x_2 gives us p(n) = x_0 + x_1*n + x_2*n^2

# solve for row echelon form, system solution will be the last column if theres
# are no zero rows, returns False if any rows become zero, otherwise True
def row_reduce(A):
    for r in A: # convert to rational numbers to ensure correct math
        for c,n in enumerate(r): r[c] = Fraction(n)
#    print(':: initial matrix')
#    for r in A: print(r)
    r = 0
    for c in range(len(A[0])): # conversion to upper triangle matrix
        if r >= len(A): break # no more rows to eliminate downward
        sr = -1 # swap row
        if A[r][c] == 0: # try to find a row without 0 to swap
            for rr in range(r+1,len(A)):
                if A[rr][c] != 0:
                    sr = rr
                    break
        if sr != -1: A[r], A[sr] = A[sr], A[r]
        if A[r][c] == 0:
            continue # couldnt find nonzero, try next column
        div = A[r][c] # divide current row to leading 1
        for cc in range(c,len(A[r])): A[r][cc] /= div
        assert A[r][c] == 1
        # add multiples of current row to lower rows to zero column c downward
        for rr in range(r+1,len(A)):
            mul = A[rr][c] # amount to multiply current row
            for cc in range(c,len(A[r])): A[rr][cc] -= mul*A[r][cc]
            assert A[rr][c] == 0
        r += 1
#    print(':: upper triangle')
#    for r in A: print(r)
    # convert to reduced row echelon form by eliminating upwards
    for r in range(len(A)-1,0,-1): # skip 0 because cant eliminate upwards
        pc = -1 # find 1 for pivot column
        for c in range(len(A[r])):
            if A[r][c] != 0:
                pc = c
                break
        if pc == -1: continue # row doesnt contain a pivot
        assert A[r][pc] == 1, str(A[r][pc])+' '+str(r)+' '+str(pc)
        for rr in range(r-1,-1,-1): # eliminate upwards
            mul = A[rr][pc]
            for c in range(pc,len(A[r])): A[rr][c] -= mul*A[r][c]
            assert A[rr][pc] == 0
#    print(':: reduced matrix')
#    for r in A: print(r)
    return True

fitsum = Fraction(0)
for terms in range(1,len(gen_poly)):
    # approximate 1 term to 10 (using degree 0 to 9 polynomials)
    A = [] # make matrix to solve
    for r in range(terms): A.append(list((r+1)**p for p in range(terms)))
    b = gen_terms[1:terms+1] # approximate with a terms-1 degree polynomial
    # we now have Ax=b so we can solve an augmented system
    for r,n in enumerate(b): A[r].append(n)
    if not row_reduce(A):
        print(': was unable to solve matrix to approximate',terms,'terms')
        break
    op = list(r[-1] for r in A) # solution in last column
    # should be correct for n=1 to n=terms so find first incorrect value (FIT)
    n = terms+1
    while eval(op,n) == eval(gen_poly,n): n += 1
    fitval = eval(op,n)
    print(': approximated',terms,'terms, FIT at n =',n,'FIT value =',fitval)
    fitsum += fitval
print(fitsum)
