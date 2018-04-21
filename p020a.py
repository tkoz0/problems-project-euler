
factorial = 100

# keep it simple by using python support for large integers
value = 1
for i in range(2, factorial+1):
    value *= i

print(':', value)
print(sum(list(int(x) for x in str(value))))

