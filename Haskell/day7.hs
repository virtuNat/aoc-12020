import System.IO
import Data.List
import Text.Regex.TDFA
import Text.Regex.TDFA.Text ()

parseLine l = concat $ map ... matches where
    matches = l =~ "([0-9]+ )?([a-z]+ [a-z]+) bag" :: [String]

matchLines ls = map parseLine lines ls

main :: IO ()
main = do
    content <- readFile "Day7Input.txt"
    print $ lines content
