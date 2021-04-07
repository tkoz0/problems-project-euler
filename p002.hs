
-- infinite list of fibonacci terms
-- the helper function fibh uses a,b as fibonacci terms
-- a is made into the list head while the parameters move forward to b,a+b
fibs :: [Integer]
fibs = let fibh a b = a : fibh b (a+b) in fibh 0 1

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
