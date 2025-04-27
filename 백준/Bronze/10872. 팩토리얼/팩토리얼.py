import sys
input=sys.stdin.readline

n=int(input())
origin=n
sum=1

for i in range(n):
    sum*=origin
    origin-=1

print(sum)