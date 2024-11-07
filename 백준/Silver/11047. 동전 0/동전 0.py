import sys
input=sys.stdin.readline

n,k=map(int,input().split())
n_list=[]
count=0

for i in range(n):
    n_list.append(int(input()))

n_list.sort(reverse=True)
#쭉 내려가다가 k가 크면, 바로 몫이랑 나누기 실행
#글고 그 나누기한 값을 바탕으로 다시 몫 저장하고 0이 될때까지 수행
for i in n_list:
    if k==0:
        break
    if i<=k:
        count+=k//i #count=4
        k%=i #k=200

print(count)