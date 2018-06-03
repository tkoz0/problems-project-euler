import math

permutations = 5

# brute force, try for each digit length

data = dict() # maps string of sorted decimal digits --> list of nums (sorted)
# list contains cube roots to save memory

minselected = 0 # used to save solution
found = False
digits = 1
while not found:
    data.clear()
    # range is 10**(digits-1) to 10**digits
    # generate data on all cubes
    cubecount = 0
    for cbrt in range(math.ceil(math.pow(10**(digits-1), 1/3)),
                      1 + math.floor(math.pow(10**digits, 1/3))):
        cube = cbrt**3
        cubecount += 1
        string = ''.join(sorted(str(cube)))
        if string in data: data[string].append(cbrt)
        else: data[string] = [cbrt]
    print(': digits =', digits, ', numcubes =', cubecount,
          ', unique digit sets =', len(data))
    # search data for a cube with required cubic permutations
    minselected = 10**digits # greater than any cube that is being tested
    maxsetsize, maxsetkey = 0, ''
    for key in data:
        l = data[key]
        if len(l) > maxsetsize: # update largest set size
            maxsetsize = len(l)
            maxsetkey = ''
        if len(l) == maxsetsize: # possible better candidate for largest set
            if maxsetkey == '' or data[key][0] < data[maxsetkey][0]:
                maxsetkey = key
        if len(l) == permutations: # required set size to find
            found = True
            minselected = min(minselected, l[0]**3)
            print(': size =', len(l), ', key =', key, ', nums =',
                  list(map(lambda x:str(x)+'^3='+str(x**3), l)))
    if maxsetkey != '':
        print(': max set, size =', len(data[maxsetkey]),
              list(map(lambda x:str(x)+'^3='+str(x**3),
                        data[maxsetkey])))
    digits += 1
print(minselected)

