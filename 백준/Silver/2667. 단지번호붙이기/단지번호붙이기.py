import sys
from collections import deque
input=sys.stdin.readline

# 상하좌우
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(graph, a, b):
    n = len(graph)
    queue = deque()
    queue.append((a, b))
    graph[a][b] = 0 # 이미 방문한 곳을 0으로 바꿔 다시 방문하지 않도록 함
    count = 1 # 해당 동에 있는 집의 개수 (디폴트: 1)

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue # 지도의 범위를 벗어나면 무시
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0 # 방문 표시
                queue.append((nx, ny))
                count += 1 # 해당 동에 있는 집의 개수 +1
    return count


# n: 지도의 크기 입력
n = int(input())
graph = []
for i in range(n):
    graph.append(list(map(int, input().strip()))) # sys.stdin.readline 사용 시, strip()함수 필수 (\n 함수가 포함되므로 제거 필요)

# 모든 위치 확인
cnt = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1: # 해당 위치가 1이라면,
            cnt.append(bfs(graph, i, j)) # bfs함수 호출, 크기를 구하고 cnt리스트에 추가

cnt.sort() # 오름차순 정렬
print(len(cnt)) # 동 개수 출력
for i in range(len(cnt)):
    print(cnt[i]) #동 크기 출력
