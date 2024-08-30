# N장의 카드, M에 최대한 가까운 카드 3장의 합

# M을 넘지 않아야함.

n,m=map(int,input().split())
np=list(map(int,input().split()))
np_sum=0

# 일단 n개의 수 중 3개를 더해서 M값에 근접하는 코드 필요
for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            current_sum=np[i]+np[j]+np[k]

            if current_sum<=m and current_sum>np_sum:
                np_sum=current_sum

print(np_sum)
                                                                                          
