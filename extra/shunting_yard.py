#!/usr/bin/env python
assoc = {'**': False} # True if left-associative
opord = {
    ':=': -2, ',': -1,
    '==': 0, '!=': 0, '<': 0, '<=': 0, '>': 0, '>=': 0,
    '|': 1, '^': 2, '&': 3,
    '<<': 4, '>>': 4,
    '+': 5, '-': 5,
    '*': 6, '/': 6, '%': 6,
    '**': 7,
    '(': 1023, ')': -1024,
    }

def shunting_yard(tokens):
    out, ops = [], []
    for t in tokens:
        if t not in opord:
            out.append(t)
            continue
        if t != '(':
            while ops and (
                opord[ops[-1]] > opord[t]
                or opord[ops[-1]] == opord[t]
                and assoc.get(ops[-1], True)
                ):
                if ops[-1] == '(':
                    if t == ')': ops.pop()
                    break
                out.append(ops.pop())
        if t != ')':
            ops.append(t)
    out.extend(ops[::-1])
    return out

print(' '.join(shunting_yard('x , y := e ** ( i * w * t + p ) , pi * e ** ( i * w * t + p ) + C'.split())))
print(' '.join(shunting_yard('x := ( 0 - b + ( b ** 2 - 4 * a * c ) ** 0.5 ) / ( 2 * a )'.split())))
