# 달팽이는 낮에 A미터 올라갈 수 있음
# But, 잠을 자는 동안 B미터 미끄러짐
# 정상에 올라간 후에는 미끄러지지 않음

# 첫째 줄에 A, B, V가 공백으로 주어짐

import math

up,down,v=map(int,input().split())

# ceil 함수: 소수점을 올림함. ex) 3.2->4, 5.7->6
days=math.ceil((v-up)/(up-down))+1

print(days)