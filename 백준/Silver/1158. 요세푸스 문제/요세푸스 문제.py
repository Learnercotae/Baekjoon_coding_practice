from collections import deque

a,b=map(int,input().split())
queue=deque(range(1,a+1))

result=[]

while queue:
    for _ in range(b-1):
        queue.append(queue.popleft())
    result.append(queue.popleft())

print("<"+", ".join(map(str,result))+">")