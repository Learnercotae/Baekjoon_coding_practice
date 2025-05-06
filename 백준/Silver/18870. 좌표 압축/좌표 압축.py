import sys
input = sys.stdin.readline

# 입력 받기
N = int(input())
nums = list(map(int, input().split()))

# 중복 제거 후 정렬
sorted_unique = sorted(set(nums))

# 각 숫자에 대해 압축된 좌표를 딕셔너리로 매핑
coord = {value: idx for idx, value in enumerate(sorted_unique)}

# 원래 입력 순서대로 압축된 값 출력
print(' '.join(str(coord[num]) for num in nums))