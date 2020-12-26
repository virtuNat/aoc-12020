import System.IO
import Data.Set (fromList, union, intersection)
import Data.List (foldl1)
import Data.List.Split

main :: IO ()
main = do
    content <- readFile "day06.txt"
    let qsets = map (map fromList . lines) $ splitOn "\n\n" content
    print $ sum $ map (length . foldl1 union) qsets
    print $ sum $ map (length . foldl1 intersection) qsets
