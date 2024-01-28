numbers = []

divby = [1,1,1,2,3,5,7,11,13,17]

def recur(number,digits):
    global numbers,divby
    if len(digits) == 0:
        numbers.append(int(''.join(map(str,number))))
    else:
        # choose a digit to append
        for d in list(digits):
            # make sure the divisibility rule is satisfied
            if 3 <= len(number) <= 9 and \
                (100*number[-2] + 10*number[-1] + d) \
                    % divby[len(number)] != 0:
                continue
            digits.remove(d)
            recur(number+[d],digits)
            digits.add(d)

recur([],set(range(10)))
print(numbers)
print(sum(numbers))
