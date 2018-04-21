
# read all data, convert to list with just the name content, then sort

data = ''
with open('data_files/p022_names.txt') as file:
    data = file.read()
data = data.split(',')
data = list(map(lambda x : x[1:-1], data))
data.sort()
print(':', len(data), 'names')

# sum scores in a loop for all names
total = 0
for i in range(len(data)):
    score = 0
    for c in data[i]:
        score += ord(c) - 64
    total += score * (i+1)
print(total)

