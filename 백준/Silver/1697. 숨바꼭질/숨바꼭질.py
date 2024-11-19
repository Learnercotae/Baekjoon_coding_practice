#deque는 리스트와 비슷하지만, 양쪽 끝에서 빠르게 요소를 추가하거나 제거할 수 있는 자료구조
#큐와 스택을 쉽게 구현할 수 있음
from collections import deque
import sys
input=sys.stdin.readline


def bfs():
    q=deque() #deque로 설정
    q.append(n) #q=deque([5])
    while q:
        x=q.popleft() #처음 시작점 x=5, q=deque([])
        if x==k:
            print(dist[x])
            break
        for nx in (x-1,x+1,x*2): #nx=4,6,10이라면
            if 0<=nx<=MAX and not dist[nx]:
                dist[nx]=dist[x]+1
                q.append(nx)

MAX=10**5 #시간초과 안나게 수 제한
dist=[0]*(MAX+1) #이동하는 거리를 알기 위한 변수
n,k=map(int,input().split())
bfs()
#BFS가 최단시간을 찾기에는 최적화 (가중치가 동일한 경우)
