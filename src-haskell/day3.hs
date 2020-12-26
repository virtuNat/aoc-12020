import System.IO

takeEvery :: Int -> [a] -> [a]
takeEvery _ [] = []
takeEvery n (x:xs) = x : takeEvery n (drop (n-1) xs)

takePath :: [String] -> Int -> Int -> [Char]
takePath [] _ _ = []
takePath (t:ts) dx x = t !! x : takePath ts dx ((x + dx) `mod` length t)

treeCount :: [String] -> Int -> Int -> Int
treeCount ts dy dx = sum $ map (fromEnum . ('#'==)) $ takePath (takeEvery dy ts) dx 0

main :: IO ()
main = do
    content <- readFile "day03.txt"
    print $ treeCount (lines content) 1 3
    print $ product [treeCount (lines content) dy dx | (dx, dy) <- [(1,1),(3,1),(5,1),(7,1),(1,2)]]
