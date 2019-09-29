
div1_20 :: Integer -> Integer -> Bool
div1_20 n d = if d > 20 then True else n `mod` d == 0 && div1_20 n (d+1)

-- check all in multiples of 20, starting with d=2
compute :: Integer -> Integer
compute n = if div1_20 n 2 then n else compute (n+20)

main = do
    putStrLn (show (compute 20)) -- start with 20
