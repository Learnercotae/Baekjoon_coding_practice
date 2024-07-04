# 서로 다른 9개의 자연수 입력 받고,
# 최대값 찾아야하며, 몇 번째 숫자였는지까지 계산하여 출력

# -for문을 이용하여 list에 저장?
# -변수 하나 추가하여 3중으로 스위치하여 최대값 저장

list=[]

for i in range(9):
    list.append(int(input())) # list 0부터 8까지 값을 입력받아 집어넣겠다.

print(max(list)) # list 값 중 가장 큰 값 출력
print(list.index(max(list))+1) # list의 가장 큰 값의 위치 +1하여 출력