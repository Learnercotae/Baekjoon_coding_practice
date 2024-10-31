import sys
# sys.stdin.readline()을 통해 입력을 빠르게 받기 위한 설정
input = sys.stdin.readline

# 해시 함수에서 사용하는 큰 소수 M과 r의 값 설정
M = 1234567891
r = 31

# 첫 번째 입력: 문자열의 길이
# 문자열 길이를 정수로 입력받음
a = int(input())

# 해시 값을 계산하기 위한 초기값 설정
answer = 0

# 문자열 입력을 받아 각 문자를 숫자로 매핑할 준비
# 입력받은 문자열을 변수 user_input에 저장
user_input = input().strip()

# 문자열의 각 문자에 대해 해시 값을 계산
for i in range(len(user_input)):
    # 각 문자를 숫자로 변환하기 위해 ord() 함수 사용
    # 'a'의 아스키 값이 97이므로 96을 빼주면 'a' -> 1, 'b' -> 2, ..., 'z' -> 26이 됨
    num = ord(user_input[i]) - 96
    # 해시 값에 num * (r^i)를 더해 누적함
    answer += num * (r ** i)

# 최종 해시 값을 M으로 나눈 나머지를 출력
print(answer % M)
