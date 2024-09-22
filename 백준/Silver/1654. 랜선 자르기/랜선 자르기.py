import sys

n,p=map(int,input().split())
m=[]

for i in range(n):
    m.append(int(sys.stdin.readline()))
    
lt,rt=1,max(m)

while lt<=rt:
    mid=(lt+rt)//2

    m_sum=0
    for i in m:
        m_sum+=i//mid

    if m_sum>=p:
        lt=mid+1
    else:
        rt=mid-1
        
print(rt)