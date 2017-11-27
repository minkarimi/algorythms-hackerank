b=int(input())
a=[int(x) for x in input().strip().split(' ')]

def insertionsort(a):
    count=0
    for i in range(1,len(a)):

        key=a[i]
        j=i-1
        while j>=0 and a[j]>key:
            a[j+1]=a[j]
            count+=1
            j=j-1
        a[j+1]=key
    return count
print(insertionsort(a))