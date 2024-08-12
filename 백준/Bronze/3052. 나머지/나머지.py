# 배열 생성 후, 입력 받을 때 나머지 값을 저장, 나머지 값이 없다면 배열에 추가
# 배열의 길이를 출

#배열 생성
b=[]

for i in range(10):
    #for문을 이용하여 입력 10번 받음
    n=int(input())%42
    #n이 b에 없다면 b배열에 추가
    if n not in b:
        b.append(n)

print(len(b))