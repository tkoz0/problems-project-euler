
-- integer square root
isqrt :: Integer -> Integer
isqrt 0 = 0
isqrt 1 = 1
isqrt n = head $ dropWhile (\x -> x*x > n) $ iterate (\x -> (x + n `div` x) `div` 2) (n `div` 2)

-- sieve of eratosthenes
sieve :: [Integer] -> [Integer] -> Integer -> [Integer]
sieve primes list@(h:t) lim =
    if h > lim then primes++list -- primes up to sqrt and remainder
    else sieve (primes++[h]) (filter (\x -> x `mod` h /= 0) t) lim

compute :: Integer -> Integer
compute n = sum (sieve [] [2..n] (isqrt n))

main = do
    putStrLn (show (compute 2000000))
