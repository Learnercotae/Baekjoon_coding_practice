import sys
input=sys.stdin.readline

n=int(input())

p=0
while n>=0:
    if n%5==0: # 5의 배수이면
        p+=(n//5) # 5로 나눈 몫을 구해야 정수가 됨
        print(p)
        break
    n-=3
    p+=1 # 5의 배수가 될 때까지 설탕 -3, 봉지+1
else:
    print(-1)
