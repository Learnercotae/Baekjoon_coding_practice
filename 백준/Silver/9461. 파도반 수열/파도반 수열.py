import sys
input=sys.stdin.readline

n=int(input())
list=[0,1,1,1,2,2,3,4,5,7,9]

for i in range(11,101):
    list.append(list[i-2]+list[i-3])

for _ in range(n):
    t=int(input())
    print(list[t])

