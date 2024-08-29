# 육각형으로 이루어진 벌집

# 1차원당 6의 배수만큼 차이가 남

num = int(input())
numbox = 1
cnt = 1

while num > numbox: # 입력받은 값이 1보다 크다면
    numbox += 6 * cnt # numbox에 6*cnt를 더한다
    cnt += 1 # 계산을 끝내고 1을 더한다
print(cnt)