# - 값 3개를 입력받아야 함.
# - 출력 시 for문을 사용하여 0부터 9까지 숫자가 몇 번 쓰였는지 확인 후 출력

a=int(input())
b=int(input())
c=int(input())

# - 일단 sum으로 곱하고, 0부터 9까지 몇 번 쓰였는지 구해야함.
# - 각 자리마다 카운트 필요 (split 사용?)
# sum=a*b*c
# al=int(sum,split())
# - 반복문으로 반복하고, 0==0이면 카운트 +1 설정
#for al in range:
#    for j in range (0,9):
#        if j==al:

sum=list(str(a*b*c)) # 문자열(str)로 변환후 list로 묶음.

for i in range(10):
    print(sum.count(str(i)))
            