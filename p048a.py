
lastdigits = 10
uppernum = 1000

# compute number
print(sum(x**x for x in range(1, uppernum+1)) % 10**lastdigits)

# use modulus (saves on memory and time, barely for this small problem)
total = 0
modulus = 10**lastdigits
for x in range(1, uppernum+1):
    val = 1
    exp = x
    base = x
    while exp != 0: # modular exponentiation by squaring
        if exp % 2 == 1: # multiply where a 1 occurs
            val = (val * base) % modulus
        base = (base * base) % modulus # square to next (base^(2^n) % mod)
        exp //= 2
    total = (total + val) % modulus
print(total)
