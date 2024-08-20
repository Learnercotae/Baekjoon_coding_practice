# 일단 알파벳 28을 -1로 쭉 깔아놓고, 입력 받은 값이랑 비교
# 만약 첫글자가 b라면 두번째 위치에 0으로 변경

a=list(input())
b='abcdefghijklmnopqrstuvwxyz'

# 알파벳 배치할 때 -1로 배치 후, 띄어쓰기 필요
for i in b:
    if i in a:
        print(a.index(i),end=' ')
    else:
        print(-1,end=' ')
    