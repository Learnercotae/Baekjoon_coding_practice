import sys
input=sys.stdin.readline

N=int(input())

array_N=[]

for i in range(N):
    a,b=input().split()
    array_N.append([int(a),b])

array_N.sort(key=lambda x: x[0]) # 나이 기준 정렬, 가입 순서 유지

for a,b in array_N:
    print(a,b)