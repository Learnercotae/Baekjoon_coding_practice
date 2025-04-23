import sys
input=sys.stdin.readline

N=map(int,input().split())

array_N=[]

for i in N:
    array_N.append(i)

array_N.sort()

print(array_N[1])