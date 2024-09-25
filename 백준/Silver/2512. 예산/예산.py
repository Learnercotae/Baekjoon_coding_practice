N=int(input())
P=list(map(int,input().split()))
P.sort()
M=int(input())
m_sum=0
lt,rt=0,max(P)

while lt<=rt:
    mid=(lt+rt)//2
    total=0

    for i in P:
        if i>mid: # P(i)가 mid보다 크다면
            total+=mid # total에 mid값 저장
        else:
            total+=i # 아니라면 total에 i값 저장
    if total<=M:
        m_sum=mid
        lt=mid+1
    else:
        rt=mid-1
print(m_sum)