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
    else if even p then -- handle evens separately
        let q = div p 2 in if q == 1 then p else compute q
    else loop p 3 -- loop over odds

-- odd loop for largest prime factor
lpf_helper :: Integer -> Integer -> Integer -> Integer
lpf_helper n d largest =
    if d*d > n then max n largest -- n will be 1 or a prime
    else if mod n d == 0 then lpf_helper (div n d) d d -- divide prime factor
    else lpf_helper n (d+2) largest

-- divides by 2 until odd
div2s :: Integer -> Integer
div2s n = if even n then div2s (div n 2) else n

-- use helper functions
largestPrimeFactor :: Integer -> Integer
largestPrimeFactor n =
    if odd n then lpf_helper n 3 1 -- use odd loop to find factors
    else lpf_helper (div2s n) 3 2 -- skip 2 and use odd loop

main = do
    putStrLn (show (compute 600851475143))
    putStrLn (show (compute 600851475143))
