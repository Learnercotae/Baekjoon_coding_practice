import sys
input=sys.stdin.readline

N=int(input())
array_N=[]

for _ in range(N):
    a,b=map(int,input().split())
    
    #튜플로 설정, (튜플: 값이 불변, 리스트: 값이 가변)
    array_N.append((a,b))

# 종료 시간 기준으로 정렬, 종료 시간이 같으면 시작 시간 기준
array_N.sort(key=lambda x: (x[1],x[0]))

cnt=0
end_time=0

for a,b in array_N:
    if a>=end_time:
        cnt+=1
        end_time=b

print(cnt)