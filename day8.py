#!/usr/bin/env python

def run(cmds):
    acc = ptr = 0
    seen = set()
    while ptr < len(cmds):
        if ptr in seen:
            return acc, False
        seen.add(ptr)
        cmd, val = cmds[ptr]
        if cmd == 'j':
            ptr += val
            continue
        if cmd == 'a':
            acc += val
        ptr += 1
    return acc, True

def main():
    with open(f'{__file__[:-3].capitalize()}Input.txt', 'r') as ifile:
        cmds = [[line[0], int(line[4:])] for line in ifile]
    print(run(cmds)[0]) #1

    for i, (cmd, _) in enumerate(cmds): # BRUTE FORCE BAYBEE
        if cmd == 'a': continue
        old = cmds[i][0]
        cmds[i][0] = {'j': 'n', 'n': 'j'}[old]
        acc, res = run(cmds)
        if res: break
        cmds[i][0] = old
    print(acc) # 2
