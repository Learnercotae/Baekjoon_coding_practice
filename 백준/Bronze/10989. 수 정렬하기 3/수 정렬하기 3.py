import sys

n = int(sys.stdin.readline())
num_list = [0] * 10001

#for문 속에서 append 사용시 메모리 재할당 때문에 효율적으로 사용 불가능

for _ in range(n):
    num_list[int(sys.stdin.readline())] += 1

for i in range(10001):
    if num_list[i] != 0:
        for j in range(num_list[i]):
            print(i)