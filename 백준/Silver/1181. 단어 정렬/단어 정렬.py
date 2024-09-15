import sys

n=int(sys.stdin.readline())
lst=[]

for i in range(n):
    lst.append(sys.stdin.readline().strip())

set_lst=set(lst) # set으로 변환해서 중복값 제거
lst=list(set_lst) # 다시 list로 변환
lst.sort() # 괄호 안에 아무 값도 넣지 않으면 알파벳 순서대로 정렬해줌
lst.sort(key=len) # 문자열 길이 순으로 정렬

for i in lst:
    print(i)