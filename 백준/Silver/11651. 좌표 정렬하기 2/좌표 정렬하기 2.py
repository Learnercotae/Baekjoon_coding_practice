import sys
input=sys.stdin.readline

N=int(input())
ary_N=[]

for i in range(N):
    a,b=map(int,input().split())
    ary_N.append((a,b))
ary_N.sort(key=lambda x:(x[1], x[0]))

for a,b in ary_N:
    print(a,b)