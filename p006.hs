
compute :: Integer -> Integer -> Integer
compute a b = (sum [a..b])^2 - sum (map (^2) [a..b])

main = do
    putStrLn (show (compute 1 100))
