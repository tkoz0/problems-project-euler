
data = ''
with open('data_files/p067_triangle.txt') as file:
    data = file.read()
data = data.splitlines() # list of rows in the triangle
for i,l in enumerate(data): # convert each row to list of integers
    data[i] = list(int(n) for n in l.split(' '))

# use dynamic programming to work backwards
for r in range(len(data)-2, -1, -1):
    for c in range(len(data[r])): # pick max sum formed starting from here down
        data[r][c] += max(data[r+1][c], data[r+1][c+1])
print(data[0][0]) # now has max solution
