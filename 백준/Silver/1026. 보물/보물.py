import sys
input=sys.stdin.readline

n=int(input())

A=[]
B=[]
all=0
all_a=0

A=list(map(int,input().split()))
B=list(map(int,input().split()))

#이중 for문은 시간복잡도가 n^2이므로 웬만해선 사용X
#for i in range(n):
    #for j in range(n):
        #ab_sum=(A[i]*B[j])
        #all+=ab_sum

        #if all_a>all:
            #all_a=all
A.sort()
B_sorted=sorted(B,reverse=True)

for i in range(n):
    ab_sum=(A[i]*B_sorted[i])
    all+=ab_sum

print(all)
