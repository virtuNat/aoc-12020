#!/usr/bin/env python
import re

def validate(ppt):
    return bool(
        1920 <= int(ppt['byr']) <= 2002
        and 2010 <= int(ppt['iyr']) <= 2020 <= int(ppt['eyr']) <= 2030
        and (150 <= int(ppt['hgt'][:-2]) <= 193 if ppt['hgt'].endswith('cm')
            else 59 <= int(ppt['hgt'][:-2]) <= 76 if ppt['hgt'].endswith('in')
            else False
            )
        and re.match(r'#[\da-f]{6}$', ppt['hcl'])
        and ppt['ecl'] in {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'}
        and re.match(r'\d{9}$', ppt['pid'])
        )

def main():
    with open(f'{__file__[:-3].capitalize()}Input.txt', 'r') as ifile:
        passes = []
        for line in ifile.read().split('\n\n'):
            ppt = dict(item.split(':') for item in line.split())
            if {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'} <= ppt.keys():
                passes.append(ppt)
    
    print(len(passes)) # 1
    print(sum(map(validate, passes))) # 2
