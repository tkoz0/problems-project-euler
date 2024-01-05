def word_form(n):
    if n < 0:
        return 'negative' + word_form(-n)
    if n < 20: # use lookup table for small numbers
        return [
            'zero', 'one', 'two', 'three', 'four', 'five',
            'six', 'seven', 'eight', 'nine', 'ten',
            'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen',
            'sixteen', 'seventeen', 'eighteen', 'nineteen'
        ][n]
    elif n < 100: # 20-99
        tens,ones = divmod(n,10)
        ret = [
            '', '', 'twenty', 'thirty', 'forty', 'fifty',
            'sixty', 'seventy', 'eighty', 'ninety'
        ][tens]
        if ones != 0:
            ret += word_form(ones)
        return ret
    elif n < 1000: # 100-999
        hundreds,remainder = divmod(n,100)
        ret = word_form(hundreds) + 'hundred'
        if remainder != 0:
            ret += 'and' + word_form(remainder)
        return ret
    else:
        raise Exception('too big')

print(sum(len(word_form(n)) for n in range(1,1000)) + len('onethousand'))
