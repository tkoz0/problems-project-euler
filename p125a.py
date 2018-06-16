import libtkoz as lib

limit = 10**8
showpalindromes = False

# pick a starting square and add consecutive squares finding palindromes,
# stop when reaching limit

start = 1
palindromes = set()
while start**2 < limit//2: # sums must have more than 1 square
    sqsum = start**2
    end = start+1
    sqsum += end**2 # add squares to make consecutive square sum
    while sqsum < limit:
        if lib.palindrome(sqsum):
            if showpalindromes:
                print(':',sqsum,'= sum squares from',start,'to',end)
            if sqsum in palindromes: print(': repeated',sqsum)
            palindromes.add(sqsum)
        end += 1
        sqsum += end**2
    start += 1
print(sum(palindromes))
