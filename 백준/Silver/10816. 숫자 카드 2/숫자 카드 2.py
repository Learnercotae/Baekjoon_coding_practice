n=int(input())
a=list(map(int,input().split()))
r=int(input())
arr=list(map(int,input().split()))
a.sort() #오름차순으로 정렬
b={} #빈 딕셔너리 생성

#리스트 a의 각 요소에 대해 등장 횟수를 딕셔너리 b에 기록
for i in a:
    #현재 요소 i가 딕셔너리 b에 존재하는지 확인
    #존재하면 True, 존재하지 않으면 False 반환
    if i in b:
        b[i]+=1
    else:
        b[i]=1

#리스트 arr의 각 요소에 대해 딕셔너리 b에서 등장 횟수 출력
for i in arr:
    if i in b:
        print(b[i],end=' ')
    else:
        print('0',end=' ')