
-- generates list of fibonacci numbers in reverse order
fibs :: Integer -> [Integer] -> [Integer]
fibs l [] = fibs l [1,0]
fibs l (h:t) = if t == [] then fibs l [1,0]
    else if h + (head t) > l then [h]++t
    else fibs l ([h + (head t)] ++ [h] ++ t)

-- from fibonacci list, filter to get evens, then sum them
compute :: Integer -> Integer
compute l = foldl (+) 0 (filter (\x -> x `mod` 2 == 0) (fibs l []))

-- alternative as 1 function: limit, a,b, sum where a,b are fibonacci terms
compute2 :: Integer -> Integer -> Integer -> Integer -> Integer
compute2 l a b s =
    if a+b > l then s
    else if (a+b) `mod` 2 == 0 then compute2 l (max a b) (a+b) (s+a+b)
    else compute2 l (max a b) (a+b) s

main = do
    putStrLn (show (compute 4000000))
    putStrLn (show (compute2 4000000 0 1 0))
