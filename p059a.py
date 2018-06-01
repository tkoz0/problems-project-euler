
keylen = 3
lower = 'abcdefghijklmnopqrstuvwxyz'
upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# brute force solution, trying all possible keys takes ~12 sec (i5-2540m)
# measure likelihood of english based on characters ETAeta which are most
# common in english words

data = ''
with open('data_files/p059_cipher.txt') as file:
    data = file.read()
data = data.split(',') # list of strings which represent integers
data = ''.join(chr(int(n)) for n in data)

def decrypt(k):
    global data
    global keylen
    plaintext = ''
    ki = 0 # index in key for xor operation
    for c in data:
        plaintext += chr(ord(c) ^ ord(k[ki]))
        ki = (ki+1) % keylen
    return plaintext

best_english_score = 0
best_key = ''

def recurse_keys(k):
    global keylen
    global lower
    global best_english_score
    global best_key
    if len(k) == keylen: # try key
        plaintext = decrypt(k)
        # measure of common english by using 3 most common letters
        score = sum(1 for c in plaintext if c in 'ETAeta')
        if score > best_english_score:
            best_key = k
            best_english_score = score
            print(': better (ETA/eta) count is', score, '( password =', k, ')')
    else:
        for c in lower:
            recurse_keys(k + c) # try all possible keys

recurse_keys('') # initiate recursion
print(': password is', best_key)
print(': message is:', decrypt(best_key))
print(sum(ord(c) for c in decrypt(best_key))) # sum ascii values
