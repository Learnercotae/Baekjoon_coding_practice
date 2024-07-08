# 문자열 S가 공백으로 구분되어 주어짐.
# 각 문자를 R번 반복하여 새 문자열 P 완성

# - 앞 숫자를 int로 받고, 뒤에 문자들을 list로 받음.
#a=int(input())
#b=list(str(input()))
#for i in range(len(b)):
    #for i in range(a):
        #print(b.str(i))


# 2를 입력받을 input을 만들고, 2의 길이만큼 for문
# b,c를 input받아주고, c의 길이만큼 문자열 반복
# end를 사용하여 붙여주고, print()를 사용하여 띄어쓰기

a= int(input())

for i in range(a):
    b,c=input().split() # - 2 abc
    for i in range(len(c)):
        print(int(b)*c[i],end='')
    print()