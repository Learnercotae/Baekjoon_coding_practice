import sys
input=sys.stdin.readline

N=int(input())
sort_N=[]

N=str(N)
for i in N:
    sort_N.append(i)

sort_N.sort(reverse=True)

for i in sort_N:
    print(i,end="")