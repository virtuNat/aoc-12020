import System.IO

combinations :: Int -> [a] -> [[a]] 
combinations 0 _ = [[]]
combinations _ [] = [[]]
combinations n (x:xs) = map (x:) (combinations (n-1) xs) ++ combinations n xs

tally :: Int -> [Int] -> Int
tally _ [] = 0
tally n xs = head [product x | x <- combinations n xs, sum x == 2020]

main :: IO ()
main = do
    content <- readFile "Day1Input.txt"
    let nlist = map read $ words content :: [Int]
    print $ tally 2 nlist
    print $ tally 3 nlist
