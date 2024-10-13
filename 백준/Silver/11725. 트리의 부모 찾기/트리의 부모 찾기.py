import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**6)

N=int(input().strip())

#빈 리스트 그래프 생성
graph=[[] for i in range(N+1)]
for i in range(N-1):
    a,b=map(int,input().strip().split())
    graph[a].append(b)
    graph[b].append(a)

#방문 여부
visited=[0]*(N+1)

def dfs(node):
    for i in graph[node]: #해당 노드에 인접한 노드 중에서
        if visited[i]==0: #방문한 적이 없다면
            visited[i]=node #해당 노드를 부모 노드로 저장
            dfs(i)

dfs(1)

for x in range(2,N+1):
    print(visited[x])
