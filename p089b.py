
data = ''
with open('data_files/p089_roman.txt') as file:
    data = file.read()
original = len(data) # characters in original data

# since the given is valid space is only saved by converting the following:
# DCCCC --> CM
# CCCC --> CD
# LXXXX --> XC
# XXXX --> XL
# VIIII --> IX
# IIII --> IV

data = data.replace('DCCCC', 'CM')
data = data.replace('CCCC', 'CD')
data = data.replace('LXXXX', 'XC')
data = data.replace('XXXX', 'XL')
data = data.replace('VIIII', 'IX')
data = data.replace('IIII', 'IV')

print(original-len(data))
