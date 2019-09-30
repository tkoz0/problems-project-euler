
factorial :: Integer -> Integer -- can be done with combinations formula
factorial n = if n == 0 then 1 else n * factorial (n-1)

-- generating pascals triangle (lazy evaluation infinite 2d list)
pascal = map (\r -> map (\c -> pasc (fst c) (snd c)) r)
             [[(x,y) | y<-[0..x]] | x<-[0..]]
    where pasc rr 0 = 1
          pasc 0 cc = 1
          pasc rr cc = if rr == cc then 1
              else pascal !! (rr-1) !! (cc-1) + pascal !! (rr-1) !! cc

-- merge by adding pairs of terms into one
pascal_row_helper :: [Integer] -> [Integer]
pascal_row_helper (a:t@(b:t2)) = [a+b] ++ pascal_row_helper t
pascal_row_helper t = []

-- generate pascal triangle row by row
pascal_row :: Integer -> [Integer]
pascal_row 0 = [1]
pascal_row 1 = [1,1]
pascal_row n = [1] ++ (pascal_row_helper (pascal_row (n-1))) ++ [1]

main = do
    putStrLn (show (div (factorial 40) (factorial 20 * factorial 20)))
    putStrLn (show (pascal_row 40 !! 20))
    putStrLn (show (pascal !! 40 !! 20))
