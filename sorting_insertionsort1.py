def insertionSort():
    for i in range(n):
        j,temp = i,0
        while j>0 and l[j]<l[j-1]:
            temp = l[j]
            l[j] = l[j-1]
            for k in range(n):
                print(l[k],end=' ')
            print()
            l[j-1] = temp
            j = j - 1
    for k in range(n):
        print(l[k],end=' ')

n = int(input())
l = list(map(int,input().split()))
insertionSort()