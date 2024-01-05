weekday = 1 # 0 = sunday, 1 = monday, ...
count = 0
for y in range(1900,2001):
    months = [31,28,31,30,31,30,31,31,30,31,30,31]
    # set february to 29 days if leap year
    if y % 4 == 0 and not (y % 100 == 0 and y % 400 != 0):
        months[1] = 29
    for m in months:
        if weekday == 0 and 1901 <= y <= 2000:
            count += 1
        weekday = (weekday + m) % 7
print(count)
