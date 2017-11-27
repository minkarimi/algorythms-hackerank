n = int(input())
ar = [int(i) for i in input().split()]
pivot = [ar[0]]
left = []
right = []
for i in range(1, n):
    if ar[i] < ar[0]:
        left.append(ar[i])
    elif ar[i] == ar[0]:
        pivot.append(ar[i])
    elif ar[i] > ar[0]:
        right.append(ar[i])
res = left + pivot + right

print(' '.join([str(i) for i in res]))