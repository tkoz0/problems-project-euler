
data = ''
with open('data_files/p089_roman.txt') as file:
    data = file.read()
data = data.splitlines()
original = sum(len(s) for s in data) # characters in original data

# I=1, V=5, X=10, L=50, C=100, D=500, M=1000
valueof = { 'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000 }
hundreds = ['', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM']
tens = ['', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC']
ones = ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX']

def minimal(roman): # convert roman numeral to its minimal representation
    global valueof
    roman = roman[::-1]
    value = 0
    prevval = 0
    for c in roman: # iterate through in reverse order
        if valueof[c] < prevval: value -= valueof[c] # out of place smaller num
        else: value += valueof[c]
        prevval = valueof[c]
    # convert to minimal valid form with conversion tables created
    conv = 'M' * (value//1000)# 1 M for each thousand
    value %= 1000
    conv += hundreds[value//100]
    value %= 100
    conv += tens[value//10]
    value %= 10
    conv += ones[value]
    return conv

data = list(minimal(s) for s in data) # convert data to minimal form
print(original-sum(len(s) for s in data)) # amount saved
