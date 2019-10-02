
-- given 1 jan 1900 is a monday

isleap y = if y `mod` 100 == 0 && y `mod` 400 /= 0 then False
    else y `mod` 4 == 0

-- ring array: loop around mod 7
ringarr startd days = if days == 0 then []
    else [startd `mod` 7] ++ ringarr (startd+1) (days-1)

-- days in a month
monthdays y m = if m == 2 then (if isleap y then 29 else 28)
    else if elem m [9,4,6,11] then 30 else 31

-- compute data, 0 = sunday, 1 = monday, ..., 6 = saturday
weekday = [ [
            -- compute day data for this month
            let startd = (if y == 1900 && m == 1 then 1
                          else if m == 1 then weekday !! (y-1-1900) !! 11 !! 30
                          else weekday !! (y-1900) !! (m-2) !! (monthdays y (m-1) - 1))
            in ringarr startd (monthdays y m)
        | m <- [1..12] ] -- months
    | y <- [1900..2000]] -- years needed to compute

main = do
    print (sum [length (filter (\x -> x!!0 == 0) (weekday !! (y-1900))) | y <- [1901..2000]])
