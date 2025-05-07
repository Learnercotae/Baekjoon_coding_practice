import sys
input=sys.stdin.readline

n=int(input())
n_list=[]
max_rope=0

for i in range(n):
    n_list.append(int(input()))

n_list.sort(reverse=True)

for i in range(n):
    a=n_list[i]*(i+1)
    if max_rope<=a:
        max_rope=a

print(max_rope)    