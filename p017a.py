
ones = ['', 'one', 'two', 'three', 'four',
        'five', 'six', 'seven', 'eight', 'nine']
tens = ['', '', 'twenty', 'thirty', 'forty',
        'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
teens = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen',
         'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']

onethousand = 'onethousand'

def one_d(n): # length of 1-9, ignore 0
    assert n < 10
    return len(ones[n])

def two_d(n): # 1-99, 1-9 special, 10-19 special
    # 20-99 are in 'tens_form' '1-9 digit form'
    assert n < 100
    if n < 10: return one_d(n)
    if n < 20: return len(teens[n-10])
    return len(tens[n//10]) + one_d(n%10)

def three_d(n): # 1-99 dealt with separately
    # hundreds are '1-9 form' 'hundred'
    # others are '1-9 form' 'hundred and' '1-99 form'
    assert n < 1000
    if n < 100: return two_d(n)
    if n % 100 == 0: return len(ones[n//100]) + len('hundred')
    else: return len(ones[n//100]) + len('hundredand') + two_d(n%100)

total = 0
for i in range(1000):
    total += three_d(i)
total += len(onethousand) # 1000 done separately
print(total)

