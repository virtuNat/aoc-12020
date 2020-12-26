import System.IO
import Data.List
import Data.List.Split
import Text.Read
import Text.Regex.TDFA
import Text.Regex.TDFA.Text ()

parsePasses :: String -> [[[String]]]
parsePasses content = map (\p -> map (splitOn ":") $ words p) $ splitOn "\n\n" content

validateFields :: [[String]] -> Bool
validateFields ppt = 7 == sum [fromEnum $ head entry == key |
    key   <- ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"],
    entry <- ppt
    ]

getByKey :: String -> [[String]] -> String
getByKey key ppt = head [last entry | entry <- ppt, head entry == key]

squeezeRange :: Int -> Int -> String -> Bool
squeezeRange a b x = a <= v && v <= b where
    v = case readMaybe x :: (Maybe Int) of
        Just x' -> x'
        Nothing -> 0

checkbyr = squeezeRange 1920 2002 . getByKey "byr"
checkiyr = squeezeRange 2010 2020 . getByKey "iyr"
checkeyr = squeezeRange 2020 2030 . getByKey "eyr"

checkhgt :: [[String]] -> Bool
checkhgt ppt = if isSuffixOf "cm" v
    then squeezeRange 150 193 $ init $ init v
    else if isSuffixOf "in" v
    then squeezeRange 59 76 $ init $ init v
    else False where
        v = getByKey "hgt" ppt

checkhcl = (\v -> v =~ "#[0-9a-f]{6}$" :: Bool) . getByKey "hcl"
checkecl = (\v -> v =~ "(amb|blu|brn|gry|grn|hzl|oth)" :: Bool) . getByKey "ecl"
checkpid = (\v -> v =~ "^[0-9]{9}$" :: Bool) . getByKey "pid"

validateValues :: [[String]] -> Bool
validateValues ppt = foldl1 (&&) $ map ($ ppt) [
    checkbyr, checkiyr, checkeyr, checkhgt,
    checkhcl, checkecl, checkpid
    ]

main :: IO ()
main = do
    content <- readFile "Day4Input.txt"
    let valids = filter validateFields $ parsePasses content
    print $ length valids
    print $ length $ filter validateValues valids
