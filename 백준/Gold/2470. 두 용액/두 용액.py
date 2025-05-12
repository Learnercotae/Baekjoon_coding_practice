import sys
input=sys.stdin.readline

n=int(input())
arr=list(map(int,input().split()))
arr.sort()

left,right=0,n-1

min_diff = float('inf')
n_left=0
n_right=0

while left<right:
    #sum은 리스트 처음과 끝을 더함
    sum=arr[left]+arr[right]

    #만약 절대값sum이 최소값보다 작다면,
    if abs(sum)<min_diff:
        #최소값=절대값sum으로 변경
        min_diff=abs(sum)
        n_left=arr[left]
        n_right=arr[right]

    if sum<0:
        left+=1
    elif sum>0:
        right-=1
    else:
        break

print(n_left,n_right)