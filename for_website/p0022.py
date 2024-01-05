file = open('0022_names.txt','r')
data = file.read()
# separate names into a list
data = data.split(',')
# remove the quotes
data = [s[1:-1] for s in data]
# sort
data.sort()

def name_value(s):
    return sum(1+ord(c)-ord('A') for c in s)

print(sum((i+1)*name_value(name) for i,name in enumerate(data)))
