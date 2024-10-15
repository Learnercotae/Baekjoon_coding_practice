import sys
input=sys.stdin.readline

#리스트에 ---저장
#3**N으로 설정
#ex) N=3이면 27개, 27//3=9부터 9*2까지 공백으로 바꿈
#다시 3등분
#다시 공백으로 바꿈
#길이가 1일때까지 반복

def cut(a,n):
    if n==1:
        return
    for i in range(a+n//3,a+(n//3)*2):
        result[i]=' '
    cut(a,n//3)
    cut(a+n//3*2,n//3)

while True:
    try:
        N=int(input())
        result=['-']*(3**N) #리스트에 저장. 3**N으로 설정
        cut(0,3**N)

        #join은 리스트의 요소를 하나의 문자열로 합치는 역할
        print(''.join(result)) #''는 각 요소 사이에 아무것도 넣지 않고 합침
    except:
        break