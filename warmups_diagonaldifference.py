#!/bin/python3

import sys

n = int(input().strip())
a = []

for a_i in range(n):
    a_t = [int(a_temp) for a_temp in input().strip().split(' ')]
    a.append(a_t[a_i] - a_t[n - a_i - 1])

print(abs(sum(a)))