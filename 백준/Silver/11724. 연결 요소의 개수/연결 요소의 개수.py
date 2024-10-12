# 방향 없는 그래프 = 양방향 그래프
import sys
sys.setrecursionlimit(2000)  # 재귀 깊이 제한 늘림(기본 재귀 깊이 제한 넘지 않도록 설정)
input=sys.stdin.readline

N,M=map(int,input().strip().split())
graph=[[] for _ in range(N+1)]

for i in range (M):
    u,v=map(int,input().strip().split())
    graph[u].append(v) # 정점 u에 v를 추가 (양방향)
    graph[v].append(u) # 정점 v에 u를 추가 (양방향)


visited=[0]*(N+1)

def dfs(x):
    visited[x]=1
    for i in graph[x]: # 정점 x에 인접한 모든 정점에 대해
        if not visited[i]: # 인접 정점이 방문되지 않았다면
            dfs(i) # dfs()함수 수행

count=0

# 모든 정점 순회
for i in range(1,N+1):
    if not visited[i]: # i가 방문되지 않았다면
        dfs(i) # dfs()함수 수행
        count+=1

print(count)


