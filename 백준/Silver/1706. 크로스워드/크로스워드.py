import sys
input=sys.stdin.readline

row, col=map(int,input().split())

a=[]
for i in range(row):
    a.append(list(input().strip()))

#for i in range(row):
#    a=list(map(int,input()))

b=[[0 for _ in range(row)]for _ in range(col)]

#전치 행렬
for i in range(row):
    for j in range(col):
        b[j][i]=a[i][j]


result=[]

for i in range(row):
    temp="" #문자열 초기화
    for j in range(col):
        if '#' == a[i][j]:
            if len(temp)>=2:
                result.append(temp)
            temp=""
        else:
            temp+=a[i][j]

    if len(temp) >=2:
        result.append(temp)

for i in range(col):
    temp="" #문자열 초기화
    for j in range(row):
        if '#' == b[i][j]:
            if len(temp)>=2:
                result.append(temp)
            temp=""
        else:
            temp+=b[i][j]

    if len(temp) >=2:
        result.append(temp)

result.sort()
print(result[0])