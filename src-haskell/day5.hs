import System.IO
import Data.Bits
import Data.Set (difference, fromList, elemAt)

parseToBinary :: Char -> Int
parseToBinary 'F' = 0
parseToBinary 'B' = 1
parseToBinary 'L' = 0
parseToBinary 'R' = 1

buildBinary :: String -> Int
buildBinary b = foldl1 (\x y -> shiftL x 1 + y) $ map parseToBinary b

main :: IO ()
main = do
    content <- readFile "Day5Input.txt"
    let seats = map buildBinary $ lines content
    print $ maximum seats
    print $ elemAt 0 $ difference (fromList [minimum seats..maximum seats]) $ fromList seats
