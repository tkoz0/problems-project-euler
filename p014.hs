
collatz_itr :: Integer -> Integer -- single iteration of collatz sequence
collatz_itr n = if n `mod` 2 == 0 then div n 2 else 3*n+1

-- computes collatz sequence of n, returns (n,length)
collatz :: Integer -> Integer -> Integer -> (Integer,Integer)
collatz n c l =
    if c == 1 then (n,l)
    else collatz n (collatz_itr c) (l+1)

find_best :: Integer -> Integer -> Integer -> Integer -> Integer
find_best n i best_num best_len =
    if i == n then best_num
    else let result@(nn,ll) = collatz i i 1 in
        if ll > best_len then find_best n (i+1) nn ll
        else find_best n (i+1) best_num best_len

compute :: Integer -> Integer
compute n = find_best n 1 1 1

main = do
    putStrLn (show (compute 1000000))
