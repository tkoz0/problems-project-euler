import libtkoz as lib

nummax = 100

def simplify_frac(n, d): # assumes 2 digit strings, returns integer tuple
    if sn[0] == sd[0]: return (int(sn[1]), int(sd[1])) # ax / ay
    if sn[0] == sd[1]: return (int(sn[1]), int(sd[0])) # ax / ya
    if sn[1] == sd[0]: return (int(sn[0]), int(sd[1])) # xa / ay
    if sn[1] == sd[1]: return (int(sn[0]), int(sd[0])) # xa / ya
    return None # if unable to find a simplification

# brute force
# n/d<1 --> n<d
product = (1, 1)
for n in range(10, nummax):
    for d in range(n+1, nummax):
        if n % 10 == 0 or d % 10 == 0:
            continue # should result in a 0 in any fraction component
        sn = str(n) # convert to strings for digits
        sd = str(d)
        simp = simplify_frac(sn, sd)
        if simp != None and simp[0] / simp[1] == n / d:
            print(':', n, '/', d, '=', simp[0], '/', simp[1])
            product = (product[0] * simp[0], product[1] * simp[1])
print(': product is', product)
gcd = lib.gcd_euclid(product[1], product[0])
print(': simplified', (product[0] // gcd, product[1] // gcd))
print(product[1] // gcd)

