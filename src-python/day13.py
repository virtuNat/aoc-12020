#!/usr/bin/env python
from math import prod
from aoc import get_input

def main():
    with get_input(__file__) as ifile:
        start = int(ifile.readline())
        sched = [
            ((cycle := int(bus)) - idx%cycle, cycle)
            for idx, bus in enumerate(ifile.readline().split(','))
            if bus != 'x'
            ]

    print(prod(min((bus - start%bus, bus) for _, bus in sched))) # 1

    rem1, mod1 = sched[0]
    for rem2, mod2 in sched[1:]: # Use CRT to combine modular equations
        ans = rem2*mod1*pow(mod1, -1, mod2) + rem1*mod2*pow(mod2, -1, mod1)
        mod1 *= mod2
        rem1 = ans % mod1
    print(rem1) # 2

if __name__ == '__main__':
    main()
