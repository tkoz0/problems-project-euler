
-- prime trial division
prime_loop :: Integer -> Integer -> Bool
prime_loop n d =
    if d*d>n then True
    else if n `mod` d == 0 then False
    else prime_loop n (d+2)

-- prime function, rule out some cases
prime :: Integer -> Bool
prime n =
    if n < 2 then False
    else if n < 4 then True
    else if n `mod` 2 == 0 then False
    else prime_loop n 3

compute :: Integer -> Integer -> Integer -> Integer
compute i p index =
    if i == index then p
    else if prime (p+2) then compute (i+1) (p+2) index -- next prime
    else compute i (p+2) index -- next number, not prime

main = do
    putStrLn (show (compute 2 3 10001)) -- start at 2nd prime which is 3
