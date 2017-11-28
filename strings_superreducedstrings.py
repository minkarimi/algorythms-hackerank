#!/bin/python3

import sys

def super_reduced_string(s):
    i = 0
    while len(s) > 0:
        if i == len(s)-1:
            return s
        else:
            if s[i] == s[i+1]:
                s = s[:i] + s[i+2:]
                i = 0
            else:
                i +=1
    return "Empty String"

s = input().strip()
result = super_reduced_string(s)
print(result)

