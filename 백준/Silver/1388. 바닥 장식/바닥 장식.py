import sys
input = sys.stdin.readline

# 입력 받기
n, m = map(int, input().split())
wood = [input().strip() for _ in range(n)]

# 방문 여부를 기록하기 위한 배열
visited = [[False] * m for _ in range(n)]

# 나무 판자 개수 세기
count = 0

# 각 좌표를 순회하며 나무 판자 개수 세기
for i in range(n):
    for j in range(m):
        if not visited[i][j]:
            count += 1  # 새로운 나무 판자를 발견했을 때 카운트 증가
            # 가로 방향 (`-`) 탐색
            if wood[i][j] == '-':
                nj = j
                while nj < m and wood[i][nj] == '-':
                    visited[i][nj] = True
                    nj += 1
            # 세로 방향 (`|`) 탐색
            elif wood[i][j] == '|':
                ni = i
                while ni < n and wood[ni][j] == '|':
                    visited[ni][j] = True
                    ni += 1

# 결과 출력
print(count)