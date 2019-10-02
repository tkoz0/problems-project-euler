
factorial n = if n == 0 then 1 else factorial (n-1) * n

digitsum n = if n < 10 then n else (n `mod` 10) + digitsum (div n 10)

main = do
    print (digitsum (factorial 100))
