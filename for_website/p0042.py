from math import sqrt
file = open('0042_words.txt','r')
# read and extract words
data = file.read()
data = data.split(',')
data = [word[1:-1] for word in data]
# compute letter sum for each word
data = [sum(1+ord(c)-ord('A') for c in word) for word in data]

def triangle(x):
    n = int(sqrt(2*x))
    return n*n + n == 2*x

# count triangle numbers
print(sum(1 for x in data if triangle(x)))
