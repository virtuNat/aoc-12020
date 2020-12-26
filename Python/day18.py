#!/usr/bin/env python
import re

opord = {'+': 0, '*': 0, '(': 1023, ')': -1024}
opmap = {'+': int.__radd__, '*': int.__rmul__}
def solve_infix(exprs):
    total = 0
    nums, ops = [], []
    for tokens in exprs:
        for t in tokens: # Shunting yard
            if t.isdigit():
                nums.append(int(t))
                continue
            if t != '(':
                while ops:
                    if opord[t] > opord[ops[-1]]: break
                    if ops[-1] == '(':
                        if t == ')': ops.pop()
                        break
                    nums.append(opmap[ops.pop()](nums.pop(), nums.pop()))
            if t != ')':
                ops.append(t)
        while ops:
            nums.append(opmap[ops.pop()](nums.pop(), nums.pop()))
        total += nums.pop()
    return total

def main():
    with open(f'{__file__[:-3].capitalize()}Input.txt', 'r') as ifile:
        exprs = [re.findall(r'\d+|[^\s]', line) for line in ifile]
    opord['+'] = 0
    print(solve_infix(exprs)) # 1
    opord['+'] = 1
    print(solve_infix(exprs)) # 2
