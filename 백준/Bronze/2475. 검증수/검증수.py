# 문제 보자마자 '아 값 입력받을때 map(int,input().split()) 이용해야지' 라는 생각해야됨.


num=map(int,input().split())
res=0
for i in num: #i를 통해 튜플 num에 저장한 값들을 사용함
    res+=i**2

print(res%10)
