import sys
sys.setrecursionlimit(2000)  # 재귀 깊이 제한을 늘려줍니다.
input = sys.stdin.readline

# 정점의 개수 N과 간선의 개수 M 입력
N, M = map(int, input().split())

# 그래프를 인접 리스트로 표현
graph = [[] for _ in range(N + 1)]

# 간선 정보 입력
for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

# 방문 여부를 확인하기 위한 리스트
visited = [False] * (N + 1)

# DFS 함수 정의
def dfs(x):
    visited[x] = True
    for neighbor in graph[x]:
        if not visited[neighbor]:
            dfs(neighbor)

# 연결 요소 개수를 세기 위한 변수
count = 0

# 모든 정점을 순회하면서 연결 요소 찾기
for i in range(1, N + 1):
    if not visited[i]:
        dfs(i)
        count += 1

# 연결 요소의 개수 출력
print(count)