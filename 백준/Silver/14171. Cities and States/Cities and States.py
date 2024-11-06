import sys
input = sys.stdin.readline
n = int(input()) 
count = 0 # 쌍 갯수 세기 
r = {}
for _ in range(n): # 도시 , 주 입력 받기 
    c,s= map(str,input().upper().split())
    c = c[:2]  # 도시는 앞에 두 글자만 보게 함 s = state(주) 의미
    
    if c == s : # 도시와 주 모두 같으면 안됨
        continue # skip 
    if (s, c) not in r:
        r[(s,c)] = 0 # 순서쌍 (s,c) 가 r에 없으면 딕셔너리에 넣어주고 값을 0으로 초기화
    r[(s,c)]+=1 # 이후 순서쌍의 갯수를 증가시켜줌
    if (c,s) in r: # r에 있는 (s,c) 와 순서를 바꾼 (c,s) 를 비교해서 공통된 special pair를 찾음 
         count += r[(c,s)] # 들어 있으면 count에 더해줌 
print(count)