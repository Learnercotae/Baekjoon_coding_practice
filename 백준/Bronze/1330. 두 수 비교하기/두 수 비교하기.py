a,b=map(int,input().split())
# split 함수로 나눌 때, 괄호에 아무것도 입력하지 않으면 공백을 기준으로 문자를 나눌 수 있음.
# map 함수를 이용하여 문자를 int 타입인 정수로 변환시켜 줌.

if a>b:
    print(">")
elif a<b:
    print("<")
else :
    print("==")
