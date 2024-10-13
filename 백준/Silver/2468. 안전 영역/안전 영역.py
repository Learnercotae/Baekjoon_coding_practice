import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

#상하좌우
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def dfs(x, y, height):
    visited[x][y] = True #현재 위치 방문 처리
    #상하좌우 이동하면서 탐색
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        #이동한 좌표가 유효하고, 방문하지 않았으며, 현재 높이보다 높은 경우 탐색 진행
        if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and graph[nx][ny] > height:
            dfs(nx, ny, height)

N = int(input().strip())
graph = [list(map(int, input().split())) for _ in range(N)]

#최대 높이 계산
max_height = max(map(max, graph))
result = 0

# 모든 높이에 대해 안전한 영역 계산
for height in range(max_height + 1):
    #매 높이마다 방문 여부 초기화
    visited = [[False] * N for _ in range(N)]
    safe_areas = 0
    #모든 지역 탐색하며 안전한 영역 개수 계산
    for i in range(N):
        for j in range(N):
            #방문x, 현재 높이보다 높은 경우 새로운 안전 영역 발견
            if not visited[i][j] and graph[i][j] > height:
                dfs(i, j, height)
                safe_areas += 1
    #최대 안전 영역 개수 갱신 
    result = max(result, safe_areas)

print(result)