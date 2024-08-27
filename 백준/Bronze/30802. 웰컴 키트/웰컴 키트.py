# 첫 줄: 참가자 수 N
# 두번째 줄: 티셔츠 사이즈별 신청자 수
# 세번째 줄: 정수 티셔츠와 펜의 묶음 수를 의미하는 정수 T와 P가 공백으로 구분

#티셔츠를 T장씩 최소 몇 묶음
#펜을 P자루씩 최대 몇 묶음 and 한 자루씩 몇개 주문


n=int(input())
a=list(map(int,input().split()))
t,p=map(int,input().split())

ans=0

# 나눈 몫에 따라 +1 해서 sum에 대입
for i in range(len(a)): #a개수 어케 세지;
    if a[i]%t==0:
        ans+=int(a[i]/t)
    else:
        ans+=(int(a[i]/t)+1)
    
print(ans)

ans2=[int(sum(a)/p),sum(a)%p]
print(*ans2)