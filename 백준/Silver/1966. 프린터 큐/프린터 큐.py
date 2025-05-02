from collections import deque
import sys
input=sys.stdin.readline

T=int(input())


for i in range(T):
    n,m=map(int,input().split())
    priorities = list(map(int, input().split()))
    queue = deque([(i, p) for i, p in enumerate(priorities)])  # (index, priority)
    count = 0

    while queue:
        current = queue.popleft()
        if any(current[1] < item[1] for item in queue):  # 우선순위 높은 게 뒤에 있으면
            queue.append(current)
        else:
            count += 1
            if current[0] == m:
                print(count)
                break