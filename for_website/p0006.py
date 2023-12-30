n = 100
square_of_sum = sum(range(1,n+1))**2
sum_of_squares = sum(i**2 for i in range(1,n+1))
print(square_of_sum - sum_of_squares)
