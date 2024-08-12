# 그 후, 값(숫자)을 입력받고 그 값이 순서가 맞다면 값 출력

# split = 공백을 기준으로 나누어 리스트로 반환
# map = 각 부분 문자열을 정수로 변환
# list = 위 결과를 리스트로 만들어 저장

a=list(map(int,input().split()))

#만약 숫자가 이어져있다면 ascending
#거꾸로라면 descending, 아니라면 mixed

if a==sorted(a):
    print('ascending')
elif a==sorted(a,reverse=True):
    print('descending')
else:
    print('mixed')
