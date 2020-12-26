#!/usr/bin/env python
from aoc import get_input

def main():
    with get_input(__file__) as ifile:
        key1, key2 = map(int, ifile)

    pkey = 1
    for loop in range(20201227):
        if pkey == key1:
            print(pow(key2, loop, 20201227)) # 1
            break
        pkey = pkey * 7 % 20201227

    print('Merry Christmas!') # 2

if __name__ == '__main__':
    main()
