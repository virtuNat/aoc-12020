#!/usr/bin/env python
import re
from aoc import get_input

def main():
    with get_input(__file__) as ifile:
        valids = [0, 0]
        for line in ifile:
            *n, letter, word = re.match(r'(\d+)-(\d+) (\w): (\w+)', line).groups()
            i, j = map(int, n)
            valids[0] += i <= word.count(letter) <= j
            valids[1] += (word[i-1] == letter) != (word[j-1] == letter)

    print(*valids, sep='\n') # 1 & 2

if __name__ == '__main__':
    main()
