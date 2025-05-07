import sys
input=sys.stdin.readline

T=int(input())
for i in range(T):
    n=int(input())
    
    #tuple=변환된 두개의 정수를 하나의 튜플로 만듬
    applicants=[tuple(map(int,input().split()))for _ in range(n)]

    applicants.sort()

    count=1 # 첫 번째 지원자는 항상 뽑힘
    min_interview=applicants[0][1]

    for i in range(1,n):
        if applicants[i][1]<min_interview:
            count+=1
            min_interview=applicants[i][1]

    print(count)