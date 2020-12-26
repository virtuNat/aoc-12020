#!/usr/bin/env python
from cmodules.van_eck import van_eck
from aoc import get_input

def main():
    with get_input(__file__) as ifile:
        seed = list(map(int, ifile.read().split(',')))

    print(van_eck(seed, 2020)) # 1
    print(van_eck(seed, 30000000)) # 2

if __name__ == '__main__':
    main()
