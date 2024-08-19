# 앞에 숫자 입력받고, 공백으로 나누는 함수 사용해서 분리
# 앞 숫자만큼 뒤 문자열 반복


a=int(input())

for i in range(a):
    # 띄어쓰기에 맞춰 값 저장
    b,c=input().split()
    for i in range(len(c)):
        print(int(b)*c[i],end='')
    print()
