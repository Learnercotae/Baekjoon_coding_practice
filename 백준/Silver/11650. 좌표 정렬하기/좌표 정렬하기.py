import sys
input=sys.stdin.readline

N=int(input())

sum=[]
for i in range(N):
    a,b=map(int,input().split())
    sum.append([a,b])

sum.sort() 

for i in sum:
    print(i[0],i[1])