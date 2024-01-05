from fractions import Fraction
product = Fraction(1)
for n in range(1,10):
    for d in range(n+1,10):
        for c in range(1,10):
            f1 = (10*n+c,10*d+c)
            f2 = (10*c+n,10*d+c)
            f3 = (10*n+c,10*c+d)
            f4 = (10*c+n,10*d+c)
            for fn,fd in [f1,f2,f3,f4]:
                if Fraction(fn,fd) == Fraction(n,d):
                    product *= Fraction(n,d)
                    print(f'found {fn}/{fd} = {n}/{d}')
print(f'product {product}')
print(product.denominator)
