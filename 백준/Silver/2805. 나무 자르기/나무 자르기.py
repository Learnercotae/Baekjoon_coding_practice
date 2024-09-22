n,m=map(int,input().split())
p=list(map(int,input().split()))
start,end=1,max(p)

while start<=end:
    mid=(start+end)//2

    p_sum=0
    for i in p:
        if i>=mid:
            p_sum+=i-mid

    if p_sum>=m:
        start=mid+1
    else:
        end=mid-1

print(end)
