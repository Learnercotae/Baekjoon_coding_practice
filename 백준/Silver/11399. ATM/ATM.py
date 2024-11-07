import sys
input=sys.stdin.readline

n=int(input())
 # 작은 숫자부터 정렬 필요
m=list(map(int,input().split()))
m.sort()

n_sum=0
sum_sum=0

for i in range(n):
    n_sum += m[i]
    sum_sum += n_sum

print(sum_sum)