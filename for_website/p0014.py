L = 1000000

cache_len = [0]*L
cache_max = [0]*L # track max in sequence (extra, unneeded)
cache_len[1] = 1
cache_max[1] = 1
for n_start in range(2,L):
    len_ = 0
    max_ = 0
    n = n_start
    while n >= n_start:
        len_ += 1
        max_ = max(max_,n)
        if n % 2 == 0:
            n //= 2
        else:
            n = 3*n + 1
    # use cache to finish
    cache_len[n_start] = len_ + cache_len[n]
    cache_max[n_start] = max(max_,cache_max[n])

# number with longest chain
max_len = max(cache_len)
max_len_nums = [i for i in range(L) if cache_len[i] == max_len]

# number with highest peak value in its chain
max_max = max(cache_max)
max_max_nums = [i for i in range(L) if cache_max[i] == max_max]

print(f'highest number iterated {max_max}')
print(f'reached from starting number(s) {max_max_nums}')
print(f'maximum chain length {max_len}')
for n in max_len_nums:
    print(f'starting number {n} reaches max of {cache_max[n]}')
    print(n)
