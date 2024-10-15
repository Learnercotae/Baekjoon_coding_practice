import sys

# 입력받기
N = int(sys.stdin.readline())
# N x N 크기의 이차원 리스트 (종이) 입력받기
paper = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

# 결과를 저장할 리스트
result = []

# 분할 정복을 이용한 색종이 자르기 함수
def solution(x, y, N):
    # 현재 영역의 첫 번째 색깔 저장
    color = paper[x][y]
    # 현재 영역이 모두 같은 색인지 확인
    for i in range(x, x + N):
        for j in range(y, y + N):
            # 하나라도 다른 색이 있으면 영역을 4등분하여 재귀 호출
            if color != paper[i][j]:
                solution(x, y, N // 2)  # 왼쪽 위 영역
                solution(x, y + N // 2, N // 2)  # 오른쪽 위 영역
                solution(x + N // 2, y, N // 2)  # 왼쪽 아래 영역
                solution(x + N // 2, y + N // 2, N // 2)  # 오른쪽 아래 영역
                return
    # 현재 영역이 모두 같은 색일 경우 결과 리스트에 추가
    if color == 0:
        result.append(0)  # 흰색 영역
    else:
        result.append(1)  # 파란색 영역

# 함수 호출 (초기 영역: (0, 0)에서 시작, 크기: N)
solution(0, 0, N)

# 결과 출력
print(result.count(0))  # 흰색 영역의 개수 출력
print(result.count(1))  # 파란색 영역의 개수 출력