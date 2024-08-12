import System.Environment

-- function to subtract test input values from 255
subtractBy1 :: [Int] -> [Int]
subtractBy1 [] = []
subtractBy1 (x:xs) = (255-x) : subtractBy1 xs

-- main function that converts code, applies subtractBy1 function, and outputs the result
main :: IO()
main = do 
    args <- getArgs
    let numbers = map read args :: [Int]
        result = subtractBy1 numbers
        resultStrings = map show result 
        outputStrings = unwords resultStrings
    putStrLn outputStrings

