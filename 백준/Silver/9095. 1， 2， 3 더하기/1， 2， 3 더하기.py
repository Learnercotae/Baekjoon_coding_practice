# 정수 n이 주어졌을 때, n을 1,2,3의 합으로 나타내는 방법의 수를 구해라

# 1. DP 배열 정의
# 2. 기본 초기화
# 3. 점화식 설정
# 4. 반복문을 통한 계산

T=int(input())

def count_ways(n):
    # dp 배열 초기화 (n+1 크기)
    dp = [0] * (n + 1)
    
    # 초기 조건 설정
    dp[0] = 1  # 0을 만드는 방법은 1가지 (아무 것도 선택하지 않는 것)
    
    # 점화식에 따라 dp 배열 채우기
    for i in range(1, n + 1):
        if i >= 1:
            dp[i] += dp[i - 1]
        if i >= 2:
            dp[i] += dp[i - 2]
        if i >= 3:
            dp[i] += dp[i - 3]
    
    return dp[n]

for i in range(0,T):
    n = int(input())
    print(count_ways(n))