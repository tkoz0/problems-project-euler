
-- first expand number into digit list, then compare it with its reversed list
palindrome_helper :: Integer -> [Integer] -> Bool
palindrome_helper n l =
    if n > 0 then palindrome_helper (div n 10) ([n `mod` 10]++l)
    else l == (reverse l)

palindrome :: Integer -> Bool
palindrome n = palindrome_helper n []

-- search products and find best, do a=999 with b=999...100, then a=998, etc
compute_helper :: Integer -> Integer -> Integer -> Integer
compute_helper a b best =
    if a < 100 then best -- done
    else if b < 100 then compute_helper (a-1) (a-1) best -- decrement a
    else if a*b > best && palindrome (a*b)
        then compute_helper a (b-1) (a*b)
    else compute_helper a (b-1) best

compute :: Integer
compute = compute_helper 999 999 0

main = do
    putStrLn (show compute)
