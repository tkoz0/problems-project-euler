import Debug.Trace

-- odd number loop for trial division
loop :: Integer -> Integer -> Integer
loop p d =
    if d*d > p then p -- dont exceed square root, p is prime
    else if p `mod` d == 0 then -- divide out, if 1 then d was the largest
        let q = div p d in if q == 1 then p else loop q d
    else loop p (d+2) -- increment to next odd number

compute :: Integer -> Integer
compute p =
    if p <= 3 then p
    else if p `mod` 2 == 0 then -- handle evens separately
        let q = div p 2 in if q == 1 then p else compute q
    else loop p 3 -- loop over odds

main = do
    putStrLn (show (compute 600851475143))
