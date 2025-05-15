n=int(input())
m=int(input())

a=list(map(int,input().split()))

#1 2 3 4 5 7
a.sort()

start=0
end=n-1
count=0

while start<end:
    total=a[start]+a[end]
    if total==m:
        count+=1
        start+=1
        end-=1
    elif total<m:
        start+=1
    else:
        end-=1

print(count)