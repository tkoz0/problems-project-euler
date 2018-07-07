
P = 61
Q = 10**7
M_e = 10 # modulus = P^M_e

# improvement, T_0*(1)+T_1*(1+p)+T_2*(1+p+p^2)+...
# to see this, write out the sums for each exponent of p
# this becomes T_0*(P^1-1)/(P-1) + T_1*(P^2-1)/(P-1) + ...
# only need to go up to (P^(M_e)-1)/(P-1) since higher exponents contribute
# nothing due to modulus

def t_gen(p):
    S0 = 290797
    while True:
        yield S0 % p
        S0 = (S0*S0) % 50515093

coeffcache = list((P**(z+1)-1)//(P-1) for z in range(M_e))

pcount = 0
tg = t_gen(P)
next(tg) # skip T_0
for q in range(1,Q+1):
    Tq = next(tg)
    pcount += Tq*coeffcache[min(len(coeffcache)-1,q-1)]
print(pcount % (P**M_e))
