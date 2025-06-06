from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
queue = deque()

for _ in range(N):
    command = input().strip().split()

    if command[0] == 'push':
        queue.append(command[1])
    
    elif command[0] == 'pop':
        if queue:
            print(queue.popleft())
        else:
            print(-1)
    
    elif command[0] == 'size':
        print(len(queue))
    
    elif command[0] == 'empty':
        print(0 if queue else 1)
    
    elif command[0] == 'front':
        if queue:
            print(queue[0])
        else:
            print(-1)
    
    elif command[0] == 'back':
        if queue:
            print(queue[-1])
        else:
            print(-1)