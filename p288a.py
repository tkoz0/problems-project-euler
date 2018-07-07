
P = 61
Q = 10**7

M_b = 61 # modulus b^e
M_e = 10

# ~4sec (pypy / i5-2540m)

def t_gen(p):
    S0 = 290797
    while True:
        yield S0 % p
        S0 = (S0*S0) % 50515093

tg = t_gen(P)
tvals = list(next(tg) for z in range(Q+1))

# the large number N(p,q) is sum of P^i * T[i] for i in range [0,Q]
# since every T[i] < P, summing T[i]*P^i for i in [0,n] < P^(i+1) (geo sum)
# to count factors of p: T_1+T_2*p+T_3*p^2+...
# for p^2 count: T_2+T_3*p+T_4*p^2+... (and so on)
pcount = 0
for e in range(1,Q+1): # sum T[e]+T[e+1]*p+... (e is exponent of p)
    # dont go on beyond p^(M_e-1) since they contribute nothing with the modulus
    pcount += sum(tvals[e+z]*(P**z) for z in range(min(M_e,Q-e+1)))
    pcount %= M_b**M_e
print(pcount)
