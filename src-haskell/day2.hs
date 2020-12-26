import System.IO
import Data.Text (count, pack)
import Text.Regex.TDFA
import Text.Regex.TDFA.Text ()

unpackLine :: String -> [String]
unpackLine line = matches
    where groups = line =~ "([0-9]+)-([0-9]+) ([a-z]): ([a-z]+)" :: (String, String, String, [String])
          (_, _, _, matches) = groups

tallyPass :: ([String] -> Bool) -> ([[String]] -> Int)
tallyPass pred = length . filter pred

verifyPass1 :: [String] -> Bool
verifyPass1 g = i <= tally && tally <= j
    where i = read $ g !! 0 :: Int
          j = read $ g !! 1 :: Int
          tally = count (pack $ g !! 2) $ pack $ g !! 3

verifyPass2 :: [String] -> Bool
verifyPass2 g = (word !! (i-1) == letter) /= (word !! (j-1) == letter)
    where i = read $ g !! 0 :: Int
          j = read $ g !! 1 :: Int
          letter = g !! 2 !! 0
          word = g !! 3

main :: IO ()
main = do
    content <- readFile "Day2Input.txt"
    let matches = map unpackLine $ lines content
    print $ tallyPass verifyPass1 matches
    print $ tallyPass verifyPass2 matches
