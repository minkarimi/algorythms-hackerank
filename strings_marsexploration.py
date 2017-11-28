#!/bin/python3

import sys

S = input().strip()

print(sum(1 for x, y in zip(S, 'SOS' * 33) if x != y))
