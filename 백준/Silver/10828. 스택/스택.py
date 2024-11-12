import sys
input=sys.stdin.readline

n=int(input())
st_list=[]

for i in range(n):
    a=input().split()

    if a[0]=='push':
        st_list.append(a[1])

    elif a[0]=='pop':
        if len(st_list)==0:
            print(-1)
        else:
            print(st_list.pop())

    elif a[0]=='size':
        print(len(st_list))

    elif a[0]=='empty':
        if len(st_list)==0:
            print(1)
        else:
            print(0)

    elif a[0]=='top':
        if len(st_list)==0:
            print(-1)
        else:
            print(st_list[-1])