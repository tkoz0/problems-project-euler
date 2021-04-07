
div3or5 :: Integer -> Bool
div3or5 i = i `mod` 3 == 0 || i `mod` 5 == 0

compute :: Integer -> Integer
compute l = sum (filter div3or5 [1..l-1])

main = do
    putStrLn (show (compute 1000))
