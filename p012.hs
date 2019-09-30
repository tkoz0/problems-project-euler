
divh2 :: Integer -> Integer -> Integer -> Integer -- trial divide odd divisors
divh2 n d count =
    if n `mod` d == 0 then divh2 (div n d) d (count+1) -- count divisor d
    -- n is 1 or prime, include product of previously counted factors d
    else if d*d > n then (if n == 1 then count+1 else 2*(count+1))
    else (count+1)*(divh2 n (d+2) 0) -- move to next divisor

divh1 :: Integer -> Integer -> Integer -- counts based on 2 divisors
divh1 n count =
    if n `mod` 2 == 0 then divh1 (div n 2) (count+1)
    else (count+1)*(divh2 n 3 0)

-- computes number of divisors, returns (n, number of divisors)
divisors :: Integer -> (Integer, Integer)
divisors n = (n, divh1 n 0)

triangles :: Integer -> [Integer] -- infinite list of triangle numbers
triangles n = [div (n*(n+1)) 2]++(triangles (n+1))

-- map triangle numbers to (n,divisors) pair, find one with divisors > 500
compute :: Integer -> Integer
compute divs = fst (head (dropWhile (\x -> (snd x) <= divs)
                                    (map divisors (triangles 1))))

main = do
    putStrLn (show (compute 500))
