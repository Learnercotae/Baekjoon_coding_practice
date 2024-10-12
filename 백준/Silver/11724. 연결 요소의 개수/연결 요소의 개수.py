# 방향 없는 그래프 = 양방향 그래프
import sys
sys.setrecursionlimit(2000)  # 재귀 깊이 제한을 늘립니다.
input=sys.stdin.readline

N,M=map(int,input().strip().split())
graph=[[] for _ in range(N+1)]

for i in range (M):
    u,v=map(int,input().strip().split())
    graph[u].append(v)
    graph[v].append(u)


visited=[0]*(N+1)

def dfs(x):
    visited[x]=1
    for i in graph[x]:
        if not visited[i]:
            dfs(i)

count=0

for i in range(1,N+1):
    if not visited[i]:
        dfs(i)
        count+=1


print(count)


