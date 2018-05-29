import math

data = ''
with open('data_files/p042_words.txt') as file:
    data = file.read()
data = data.split(',') # make into list of the words
data = list(map(lambda x : x[1:-1], data)) # remove ""
# convert each word to integer my summing its letters
data = list(map(lambda w : sum(1+ord(c)-ord('A') for c in w), data))

# determining if number is triangle
# suppose x=(n^2+n)/2, x can be expressed this way with n and is triangle
# 2x=n^2+n --> n^2<2x<(n+1)^2 --> n<floor(sqrt(2x))<n+1
# pick n=floor(sqrt(2x)) and determine if n^2+n=2x
def is_triangle(x):
    n = int(math.sqrt(2*x))
    return n**2 + n == 2*x

count = 0
for i in data:
    if is_triangle(i): count += 1
print(count)
