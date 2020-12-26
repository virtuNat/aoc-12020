#!/usr/bin/env python
from aoc import get_input

def main():
    with get_input(__file__) as ifile:
        steps = [line.split(' = ') for line in ifile]

    mem = {}
    for cmd, val in steps:
        if cmd == 'mask':
            masks = (int(val.replace('X', '0'), 2), int(val.replace('X', '1'), 2))
        else:
            mem[int(cmd[4:-1])] = (int(val) | masks[0]) & masks[1]
    print(sum(mem.values())) # 1

    mem = {}
    for cmd, val in steps:
        if cmd == 'mask':
            mask1 = int(val.replace('X', '0'), 2)
            maskX = val[-2::-1]
        else:
            addrs = [int(cmd[4:-1]) | mask1]
            atemp = []
            bit = 1
            for c in maskX:
                if c == 'X':
                    atemp[:] = addrs[:]
                    addrs.clear()
                    for addr in atemp:
                        addrs.extend((addr | bit, addr & (0xFFFFFFFFF ^ bit)))
                bit <<= 1
            mem.update(dict.fromkeys(addrs, int(val)))
    print(sum(mem.values())) # 2

if __name__ == '__main__':
    main()
