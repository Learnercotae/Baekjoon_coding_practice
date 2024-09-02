# 맨 앞이랑 맨 뒤랑 같은거 확인하면 끝
# index(0)이랑 index(-1)이랑 비교하면 되는거 아닌가?


while True:
    n=input()

    if n=='0':
        break

    if n==n[::-1]: # 문자열 'n'의 역순을 의미
        print('yes')
    else:
        print('no')

