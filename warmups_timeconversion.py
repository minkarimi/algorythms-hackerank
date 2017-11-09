#!/bin/python3

import sys

def timeConversion(s):
    if s[0:2] == '12':
        s = '00' + s[2:]
    if s[-2] == 'P':
        s = chr(ord(s[0])+1) + chr(ord(s[1])+2) + s[2:]
    return s[0:-2]

s = input().strip()
result = timeConversion(s)
print(result)