N = int(input())
L = list(map(int,input().split()))
print(*list(L.count(i) for i in range(100)),sep = " ")