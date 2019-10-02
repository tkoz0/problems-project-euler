
word :: Integer -> String
word n =
    let ones = word (n `mod` 10) in let hundreds = word (div n 100) in
    if n == 1000 then "onethousand" -- special case
    else if n == 0 then "" -- for usability with recursion
    else if n == 1 then "one"
    else if n == 2 then "two"
    else if n == 3 then "three"
    else if n == 4 then "four"
    else if n == 5 then "five"
    else if n == 6 then "six"
    else if n == 7 then "seven"
    else if n == 8 then "eight"
    else if n == 9 then "nine"
    else if n == 10 then "ten"
    else if n == 11 then "eleven"
    else if n == 12 then "twelve"
    else if n == 13 then "thirteen"
    else if n == 14 then "fourteen"
    else if n == 15 then "fifteen"
    else if n == 16 then "sixteen"
    else if n == 17 then "seventeen"
    else if n == 18 then "eighteen"
    else if n == 19 then "nineteen"
    else if n < 30 then "twenty" ++ ones
    else if n < 40 then "thirty" ++ ones
    else if n < 50 then "forty" ++ ones
    else if n < 60 then "fifty" ++ ones
    else if n < 70 then "sixty" ++ ones
    else if n < 80 then "seventy" ++ ones
    else if n < 90 then "eighty" ++ ones
    else if n < 100 then "ninety" ++ ones
    else if n `mod` 100 == 0 then hundreds ++ "hundred"
    else hundreds ++ "hundredand" ++ word (n `mod` 100)

compute = sum [length (word x) | x <- [1..1000]]

main = do
    print compute
