
digitsum :: Integer -> Integer
digitsum n = if n < 10 then n else (n `mod` 10) + digitsum (div n 10)

compute :: Integer -> Integer
compute p = digitsum (2^p)

main = do
    print (compute 1000)
