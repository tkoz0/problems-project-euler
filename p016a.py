
base = 2
exp = 1000

# use simple python features to do this
# compute number, convert to string, convert to list of digits as integers
# from there its just the sum of those integers (which are the digits)
print(sum(list(int(x) for x in str(base**exp))))
