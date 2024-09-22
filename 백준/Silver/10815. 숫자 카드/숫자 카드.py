import sys

n=int(sys.stdin.readline())
N=list(map(int,sys.stdin.readline().split()))
N.sort()

m=int(sys.stdin.readline())
M=list(map(int,sys.stdin.readline().split()))


for i in M:
    lt,rt=0,n-1
    exist=False

    while lt<=rt:
        mid=(lt+rt)//2

        if N[mid]>i: # 중간 값이 찾는 값보다 크다면
            rt=mid-1 # 중간보다 왼쪽 한 칸 옆까지

        elif N[mid]<i: # 중간 값이 찾는 값보다 작다면
            lt=mid+1 # 중간보다 오른쪽 한 칸 옆부터

        else:
            exist=True
            break

    print(1 if exist else 0,end=' ')