#!/bin/python3

import sys
#ascii A-Z:65-90 && a-z:97-122



n = int(input().strip())
s = input().strip()
k = int(input().strip())
for i in s:
 a=65 if i.isupper() else 97
 print((chr(a+(ord(i)-a+k)%26)) if i.isupper() or i.islower() else i ,end='')