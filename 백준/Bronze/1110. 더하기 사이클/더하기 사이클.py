import sys
input=sys.stdin.readline

n=int(input())
origin=n
cnt=0

while True:
    a=n//10
    b=n%10
    n=(b*10)+((a+b)%10)
    cnt+=1
    if n==origin:
        break


print(cnt)


