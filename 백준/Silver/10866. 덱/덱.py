from collections import deque

queue=deque()

N=int(input())

for i in range(N):
    a=input().strip().split()
    if a[0]=='push_front':
        queue.appendleft(a[1])
    elif a[0]=='push_back':
        queue.append(a[1])
    elif a[0]=='pop_front':
        if queue:
            print(queue.popleft())
        else:
            print(-1)
    elif a[0]=='pop_back':
        if queue:
            print(queue.pop())
        else:
            print(-1)
    elif a[0]=='size':
        print(len(queue))
    elif a[0]=='empty':
        if queue:
            print(0)
        else:
            print(1)
    elif a[0]=='front':
        if queue:
            print(queue[0])
        else:
            print(-1)
    elif a[0]=='back':
        if queue:
            print(queue[-1])
        else:
            print(-1)
