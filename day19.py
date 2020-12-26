#!/usr/bin/env python
import re

def main():
    with open(f'{__file__[:-3].capitalize()}Input.txt', 'r') as ifile:
        lines, msgs = ifile.read().split('\n\n')
    msgs = msgs.split()
    rules = {}
    for line in lines.split('\n'):
        i, r = line.split(': ')
        rules[i] = r[1] if r[1].isalpha() else f'({r})'

    done = False
    while not done:
        done = True
        for key, rule in rules.items():
            if any(c.isdigit() for c in rule):
                done = False
                rules[key] = re.sub(r'\d+', lambda m: rules[m.group()], rule)
    rule = rules['0'].replace(' ', '') + '$'
    print(sum(bool(re.match(rule, msg)) for msg in msgs)) # 1

    rule = re.sub(
        r'\d+', lambda m: rules[m.group()],
        f'42+ 42 {"( 42 "*6}31{" )? 31"*6}$'
        ).replace(' ', '')
    print(sum(bool(re.match(rule, msg)) for msg in msgs)) # 2
