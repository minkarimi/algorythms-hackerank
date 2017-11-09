#!/bin/python3

import sys


n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]
a = [0 if i is 0 else i/abs(i) for i in arr]

for num in map(a.count, [1, -1, 0]):
    print(round(num/n, 6))