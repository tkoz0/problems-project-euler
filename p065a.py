
# brute force compute fraction and sum digits
# based on sqrt(2) example, given the constants in a list [a, b, ..., y, z]
# the process goes like this (invert means raise to -1 power or flip fraction)
# add z, invert, add y, invert, ..., add b, invert, add a

# given e = [2; 1,2,1, 1,4,1, 1,6,1, ...]

expansion_index = 100

def e_val(n): # computes constant for the expansion of e
    if n == 0: return 2
    n += 2
    if n % 3 == 1: return (n // 3) * 2
    else: return 1

n, d = 0, 1
for i in range(expansion_index - 1, -1, -1):
    next = e_val(i)
    n += next*d # add value
    if i != 0: # invert for next iteration
        n, d = d, n
print(': expansion', expansion_index, ' =', n, '/', d)
print(': approximation', n/d)
print(sum(int(d) for d in str(n)))

# computing just the numerator
# regular continued fractions satisfy the recurrence
# h_n / k_n = (a_n * h_n-1 + h_n-2) / (a_n * k_n-1 + k_n-2)

a, b = 0, 1 # begin sequence with 0 and 1
for i in range(expansion_index): # indexes 0 to 99 for constants
    a, b = b, e_val(i) * b + a
print(': expansion', expansion_index, 'has numerator', b)
print(sum(int(d) for d in str(b)))

