#!/bin/python3

import sys
index = int(input())
for _ in range(index):
    s = input().strip()
    l = len(s)
    count = 0
    for i in 'hackerrank':
        if s.find(i,count) >= count:
            s, count = s.replace(i,"",1), s.find(i,count)
        else:
            print("NO")
            break
    if l-10 == len(s):
        print("YES")