n=int(input())
a=list(map(int,input().split()))
m=int(input())
arr=list(map(int,input().split()))
a.sort()

for i in arr:
    lt,rt=0,n-1 #lt는 맨 앞, rt는 맨 뒤
    isExist=False #찾음 여부

    #이분탐색 시작
    while lt<=rt: #lt가 rt보다 커지면 반복문 탈출
        mid=(lt+rt)//2 #mid는 중간값
        if i==a[mid]: #i(목표값)가 a[mid]값과 같다면 (목표값 존재여부를 알았다면)
            isExist=True #True로 변경
            print(1) 
            break # 1출력 후 반복문 탈출
        elif i>a[mid]: #a[mid]가 num보다 작으면
            lt=mid+1 #lt를 높임
        else: #a[mid]가 num보다 크다면
            rt=mid-1 #rt를 낮춤

    if not isExist: #못찾은 경우
        print(0) #0 출력