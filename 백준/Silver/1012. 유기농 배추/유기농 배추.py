#BFS
# 백준은 재귀의 최대 깊이가 1000으로 설정

# 행렬 생성, 1인 경우 BFS로 실행. 실행될 때마다 cnt+=1
# BFS 함수가 인접한 모든 1을 0으로 바꾸고 연결된 하나의 블럭 개수를 구할 수 있음

T=int(input())# 테스트 케이스 받는 부분

# 상하좌우 이동하여 계산하기 위한 list
dx=[-1,1,0,0] #-1은 위, 1은 아래
dy=[0,0,-1,1] # -1은 왼쪽, 1은 오른쪽

def BFS(x,y):
    queue=[(x,y)]
    matrix[x][y] = 0 # 방문처리(1이였던 값을 0으로 바꾸어 탐색 완료 표시)

    while queue:
        x,y = queue.pop(0)

        for i in range(4): #상하좌우로 이동하기 위한 반복문
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= M or ny < 0 or ny >= N: #행렬 밖으로 나가는 경우 방지
                continue

            # 주변에 같은 1이 있을 경우 
            if matrix[nx][ny] == 1 : # 1이 있다면 큐에 추가하고 방문처리
                queue.append((nx,ny))
                matrix[nx][ny] = 0

# 행렬만들기
for i in range(T): #테스트 케이스 처리
    M, N, K = map(int,input().split())
    matrix = [[0]*(N) for _ in range(M)]
    cnt = 0 # 1의 그룹을 세기 위한 변수

    # K개의 좌표에 대해 1설정
    for j in range(K):
        x,y = map(int, input().split())
        matrix[x][y] = 1

    # 행렬을 탐색하여 1이 있는 위치를 찾음
    for a in range(M):
        for b in range(N):
            if matrix[a][b] == 1: # 방문하지 않은 1발견시, BFS 호출하여 연결된 1탐색
                BFS(a,b)
                cnt += 1 #연결된 그룹 발견시 카운터 증가

    print(cnt) #테스트 케이스에서 발견된 연결 그룹 수 출력