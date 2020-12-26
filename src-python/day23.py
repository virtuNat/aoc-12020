#!/usr/bin/env python
from cmodules.cup_game import play
from aoc import get_input

def main():
    with get_input(__file__) as ifile:
        cups = tuple(int(i)-1 for i in ifile.read().strip())

    clist = play(cups, 9, 100)
    pivot = clist[0]
    while pivot != 0:
        print(pivot + 1, end='')
        pivot = clist[pivot]
    print() # 1

    clist = play(cups, 1000000, 10000000)
    x = clist[0]; y = clist[x]
    print((x + 1)*(y + 1)) # 2

if __name__ == '__main__':
    main()
