import math

# f(n,d) = occurrences of digit d in a list of numbers 0 through n
# out of all s digit numbers, d != 0 occurs s*10^(s-1) times

def slow_f(n,d):
    assert d in range(10)
    digit = str(d)
    return sum(str(i).count(digit) for i in range(n+1))

def f(n,d):
    assert d in range(1,10)
    count = 0
    if n < 10: # base case
        return 1 if n >= d else 0
    # count numbers with fewer digits than n
    n_digits = len(str(n))
    count += (n_digits-1)*10**(n_digits-2)
    # this considers 0 as a leading placeholder
    # d=0 is not allowed so that simplifies this a bit
    #n_decomposition = list(map(int,list(str(n))))
    left_digit = int(str(n)[0])
    # only count numbers with same number of digits as n
    count += (left_digit-1)*(n_digits-1)*10**(n_digits-2)
    if d < left_digit:
        count += 10**(n_digits-1)
    # numbers with same leading digit
    n2 = n - left_digit*10**(n_digits-1)
    if left_digit == d:
        count += n2+1 # count when all zeroes as well
    count += f(n2,d)
    #print('f(%d,%d)=%d'%(n,d,count))
    return count

def count_d(d,lo,hi):
    return f(hi,d)-f(lo-1,d)

s_table = [[] for _ in range(10)]

for d in range(1,10):
    n = 0
    fn = f(n,d)
    bestlog2 = 0
    while True:
        if n >= 2**50: # unproven upper bound
            break
        if int(math.log2(n+1)) > bestlog2:
            #print('reached',n,'diff =',fn-n,'log2 =',int(math.log2(n)))
            bestlog2 = int(math.log2(n))
        if n == fn:
            s_table[d].append(n)
            #print(n)
        n_digits = len(str(n))
        step = min((10**n_digits-n)//n_digits,abs(n-fn)//n_digits)
        if step == 0:
            step = 1
        n += step
        fn = f(n,d)

total_sum = 0
for d in range(1,10):
    print(': digit = %d, s_table[%d] = %s'%(d,d,str(s_table[d])))
    total_sum += sum(s_table[d])
print(total_sum)

# list of some values n for f(n,1)=1 (turns out this is all of them)
'''
0
1
199981
199982
199983
199984
199985
199986
199987
199988
199989
199990
200000
200001
1599981
1599982
1599983
1599984
1599985
1599986
1599987
1599988
1599989
1599990
2600000
2600001
13199998
35000000
35000001
35199981
35199982
35199983
35199984
35199985
35199986
35199987
35199988
35199989
35199990
35200000
35200001
117463825
500000000
500000001
500199981
500199982
500199983
500199984
500199985
500199986
500199987
500199988
500199989
500199990
500200000
500200001
501599981
501599982
501599983
501599984
501599985
501599986
501599987
501599988
501599989
501599990
502600000
502600001
513199998
535000000
535000001
535199981
535199982
535199983
535199984
535199985
535199986
535199987
535199988
535199989
535199990
535200000
535200001
1111111110
'''

