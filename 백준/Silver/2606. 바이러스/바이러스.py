import sys
input=sys.stdin.readline

N=int(input())
V=int(input())

graph=[[] for _ in range(N+1)]
for i in range(V):
    a,b=map(int,input().split())
    graph[a]+=[b] # a에 b 연결
    graph[b]+=[a] # b에 a 연결 -> 양방향

visited=[0]*(N+1)

def dfs(V):
    visited[V]=1
    for nx in graph[V]:
        if visited[nx]==0:
            dfs(nx)

dfs(1)
print(sum(visited)-1)