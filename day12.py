#!/usr/bin/env python

def navigate(path, waypt, waynav):
    pos = 0j
    for d, n in path:
        if d in 'NEWS':
            val = n * (1j ** 'ENWS'.index(d))
            if waynav:
                waypt += val
            else:
                pos += val
        elif d in 'LR':
            waypt *= (1j,-1j)['LR'.index(d)] ** (n // 90)
        else:
            pos += n * waypt
    return int(abs(pos.real) + abs(pos.imag))

def main():
    with open(f'{__file__[:-3].capitalize()}Input.txt', 'r') as ifile:
        path = [(line[0], int(line[1:])) for line in ifile]
    print(navigate(path, 1+0j, False)) # 1
    print(navigate(path, 10+1j, True)) # 2
