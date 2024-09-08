# 3킬로 봉지와 5킬로 봉지가 있음.

# 첫째 줄: N
# N을 입력받고, 먼저 N을 5로 나눈 뒤, 나머지를 3으로 나눔.

n=int(input())


# ex) 6일때는, 먼저 5로 나누어서 안되니까, 3으로 넘어가서 2를 출력해야함.


if n%5 ==0: # 5로 나누어 떨어질 때
    print(n//5)
else:
    p=0
    while n>0:
        n-=3
        p+=1
        if n%5==0: # 3Kg과 5Kg을 조합해서 담을 수 있을 때
            p+=n//5
            print(p)
            break
        elif n==1 or n==2: # 설탕 봉지만으로 나눌 수 없을 때
            print(-1)
            break
        elif n==0:
            print(p) # 3으로 나누어 떨어질 때
            break
