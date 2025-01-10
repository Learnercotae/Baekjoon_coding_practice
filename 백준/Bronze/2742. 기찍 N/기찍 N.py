import sys
input=sys.stdin.readline

a=int(input())

for i in range(a):
    print(a)
    a-=1
    if a<0:
        break
