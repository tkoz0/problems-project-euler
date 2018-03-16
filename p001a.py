MAXN = 1000

# The trivial solution is a loop with a condition for summing

sum_ = 0
for i in range(MAXN):
    if i % 3 == 0 or i % 5 == 0:
        sum_ += i
print(sum_)

# Here is a 1 line solution for that
print(sum(x for x in range(MAXN) if x % 3 == 0 or x % 5 == 0))

# Using summation formula 1+2+...+n = n(n+1)/2
# (3+6+...) + (5+10+...) - (15+30+...)
# Sum required multiples of 3 and 5 and subtract the ones summed twice
intsum = lambda x : x * (x + 1) // 2 # 1+2+...+x
max_ = MAXN - 1
threes = 3 * intsum(max_ // 3)
fives = 5 * intsum(max_ // 5)
fifteens = 15 * intsum(max_ // 15)
sum_ = threes + fives - fifteens
print(sum_)
