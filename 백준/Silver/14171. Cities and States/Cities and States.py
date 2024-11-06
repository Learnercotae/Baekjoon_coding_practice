import sys
input=sys.stdin.readline

n=int(input())
count=0
r={} # 딕셔너리 생성

for _ in range(n):
    # c=city s=state
    c,s=map(str,input().upper().split())
    # 앞 두글자만 보게 함
    c=c[:2]
    #도시와 주 모두 같으면 안됨
    if c==s:
        continue
    if (s,c) not in r: #순서쌍 (s,c)에 r이 없으면
        r[(s,c)]=0  #딕셔너리에 넣어주고 값을 0으로 초기화

    r[(s,c)]+=1 #이후 순서쌍의 개수 증가
    if (c,s) in r: #r에 있는 (s,c)와 순서를 바꾼 (c,s)를비교
        count+=r[(c,s)] #들어 있으면 count에 더해줌
print(count)
    
#리스트[], 딕셔너리{}, 튜플()
