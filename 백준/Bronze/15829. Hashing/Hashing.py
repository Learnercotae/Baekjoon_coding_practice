l=int(input())
m=1234567891
r=31

user_input=input()

answer=0

for i in range(len(user_input)):
    #ord란? 문자 -> 숫자 변환을 해주는 함수
    num=ord(user_input[i])-96
    answer+=num*(r**i)

print(answer%m)