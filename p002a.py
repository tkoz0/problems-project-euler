MAXV = 4000000

# trivial recursive fibonacci, exponential time
# takes a few seconds (i7-7600u)
def fib(n):
    if n == 0: return 0
    if n == 1: return 1
    return fib(n-1) + fib(n-2)

# use of trivial recursion
sum_ = 0
i = 0
while True:
    value = fib(i)
    if value > MAXV: break # limit for this problem
    if value % 2 == 0:
        sum_ += value
    i += 1
print(sum_)
