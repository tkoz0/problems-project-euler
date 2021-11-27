
# returns (-1+i)**p as (real,imag)
def base_power(p):
    # patterns of direction vector modulo 8 (cos(..) + i*sin(..))
    # cos(3pi*n/4) = 1, -sqrt(2)/2, 0, sqrt(2)/2, -1, sqrt(2)/2, 0, -sqrt(2)/2
    # sin(3pi*n/4) = 0, sqrt(2)/2, -1, sqrt(2)/2, 0, -sqrt(2)/2, 1, -sqrt(2)/2
    if p % 2 == 0:
        # 2^(p/2) * (cos(3pi*n/4) + i*sin(3pi*n/4))
        real = [1,0,-1,0][(p%8)//2]
        imag = [0,-1,0,1][(p%8)//2]
    else:
        real = [-1,1,1,-1][(p%8)//2]
        imag = [1,1,-1,-1][(p%8)//2]
    return (2**(p//2)*real, 2**(p//2)*imag)

def vec_sum(vecs):
    return (sum(v[0] for v in vecs),sum(v[1] for v in vecs))

L = 500
# grid for a+bi, |a|<=L, |b|<=L
grid = [[False]*(2*L+1) for _ in range(2*L+1)]
count = (2*L+1)**2

bases = [base_power(0)]
grid[L][L] = True # 0+0i
r,i = bases[0]
grid[L+r][L+i] = True # 1+0i
count -= 2 # 2 spaces filled in the grid

BL = 1 # compute B(L)

import png

while count != 0:
    bits = len(bases)
    nums = 2**bits
    bases.append(base_power(len(bases)))
    for n in range(nums):
        r,i = vec_sum([bases[-1]]
                    + [bases[z] for z in range(bits) if n & (1 << z)])
        if r < -L or r > L or i < -L or i > L:
            continue # outside the grid
        assert not grid[L+r][L+i] # should be new number
        grid[L+r][L+i] = True
        count -= 1
        BL += 1 + sum(1 for z in range(bits) if n & (1 << z))
    print(f'power {bits} done, {2**(bits+1)} numbers, {count} grid spaces left')
    img = png.from_array([[255 if z else 0 for z in row] for row in grid],'L')
    img.save(f'p508_p{bits:02}.png')

print(f'B({L}) = {BL}')
