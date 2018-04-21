
start = (1901, 1, 1) # 1901, jan 1
end = (2000, 12, 31) # 2000, dec 31
weekday = 0 # sunday
monthday = 1 # the 1st
# week days are 0=sunday, 1=monday, ..., 6=saturday
given = ((1900, 1, 1), 1) # 1900, jan 1, monday
assert given[0][2] == 1

monthdays = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def is_leap(y): # div by 4 if not century, century if divisible by 400
    if y % 400 == 0: return True
    if y % 100 == 0: return False
    return y % 4 == 0

def cmpdates(a, b): # compares 2 dates (tuples)
    if a[0] != b[0]: return a[0] < b[0]
    if a[1] != b[1]: return a[1] < b[1]
    return a[2] < b[2]

# determine starting day (with day same as month day)
counted = 0

# go back in time
date = ((given[0][0], given[0][1], given[0][2]), given[1])
while cmpdates(start, date[0]):
    year = date[0][0]
    month = date[0][1]-1
    if month == 0: # wrap from january to december
        month = 12
        year -= 1
    daysback = 0
    if month == 2 and is_leap(year): daysback = 29
    else: daysback = monthdays[month]
    date = ((year, month, 1), (date[1]-daysback)%7)
    if cmpdates(end, date[0]): continue # date not in range
    if (date[1]+(monthday-1))%7 == weekday:
        print(':', date)
        counted += 1

# go forward in time
date = ((given[0][0], given[0][1], given[0][2]), given[1])
while cmpdates(date[0], end):
    year = date[0][0]
    month = date[0][1]
    daysforward = 0
    if month == 2 and is_leap(year): daysforward = 29
    else: daysforward = monthdays[month]
    month += 1
    if month == 13: # wrap from december to january
        month = 1
        year += 1
    date = ((year, month, 1), (date[1]+daysforward)%7)
    if cmpdates(date[0], start): continue # date not in range
    if (date[1]+(monthday-1))%7 == weekday:
        print(':', date)
        counted += 1

# consider the reference date itself
if given[1] == weekday: counted += 1

print(counted)
