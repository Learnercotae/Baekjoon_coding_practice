#소수를 찾는 조건

#1은 제외
#2의 배수 제외
#3의 배수 제외
#5의 배수 제외
#7의 배수 제외
 
a=int(input())
b=list(map(int,input().split()))
ans=0

for x in b:
    for i in range(2,x+1):
        if x%i ==0:
            if x==i:
                ans+=1
            break
print(ans)