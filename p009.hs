
-- a <= b <= c, a+b+c=1000
-- a <= 333
compute :: Integer -> Integer -> Integer
compute a b = let c = 1000-a-b in
    if c < b then compute (a+1) (a+1) -- increment to next a
    else if a*a+b*b==c*c then a*b*c
    else compute a (b+1)

main = do
    putStrLn (show (compute 1 1))
