def DFS(s): # 깊이 우선 탐색
    global result # global: 함수 안에서 전역 변수 사용하기 위함

    if len(s)==1: # 길이가 1이면
        result="AKARAKA" # 조건 만족하므로 아카라카 출력
        return # 종료
    else:
        if s!=s[::-1]: # 회문이 아닌 경우, 문자열 s를 뒤집은 것
            return # 아무것도 안하고 종료
        else: # 회문인 경우
            N=len(s)//2 # 문자열을 반으로 나눠 각각 DFS 호출
            DFS(s[:N]) # 앞쪽 절반 DFS 호출
            DFS(s[-N:]) # 뒤쪽 절반 DFS 호출
s=input()

result="IPSELENTI" # 초기값을 입실렌티로 설정
DFS(s)

print(result)