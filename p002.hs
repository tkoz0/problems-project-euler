
-- infinite list of fibonacci terms helper function
-- a,b form the last 2 terms, use first as head and move forward to b,a+b
fib_helper :: Integer -> Integer -> [Integer]
fib_helper a b = a : fib_helper b (a+b)

-- infinite list of fibonacci terms
fibs :: [Integer]
fibs = fib_helper 0 1 -- start terms are 0,1

-- simple solution, get numbers up to limit, keep evens, compute sum
compute :: Integer -> Integer
compute l = sum $ filter even $ takeWhile (<l) fibs

-- alternative as 1 function: limit, a,b, sum where a,b are fibonacci terms
compute2 :: Integer -> Integer -> Integer -> Integer -> Integer
compute2 l a b s =
    if a+b > l then s
    else if even (a+b) then compute2 l (max a b) (a+b) (s+a+b)
    else compute2 l (max a b) (a+b) s

main = do
    putStrLn (show (compute 4000000))
    putStrLn (show (compute2 4000000 0 1 0))
