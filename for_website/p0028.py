S = 1001
size = 1
step = 2
diagsum = 1
number = 1
while size < S:
    size += 2
    # add the 4 corner numbers
    for _ in range(4):
        number += step
        diagsum += number
    step += 2
print(diagsum)
