# a층의 b호에 살려면 자신의 아래(a-1)층의 1호부터 b호까지 사람들 수의 합만큼
# 사람들을 데려와 살아야 함

# 아파트에 비어있는 집은 없음
# 모든 거주민들이 이 계약을 지키고 들어옴
# k층에 n호에는 몇 명이 사는지 출력
# 단, 아파트는 0층부터 있고 각 층에는 1호부터 있으며, 0층의 i호에는 i명이 산다.

# 첫째 줄: Test case의 수 T가 주어짐.

# ***************재귀함수 풀이법*************
# def n_people(a,b):
    # if a==0:
        # return b
    # return sum(n_people(a-1,i)for i in range(1,b+1)) # 뒤에 먼저 해석
                # ex) a=2 b=3 이면 range(1,4) 가 i가 됨.
                # 그래서 n_people(1,i)는 n_people(1,1) + n_people(1,2) + n_people(1,3)이 됨.

T=int(input())

for i in range(T):
    k=int(input())
    n=int(input())
    people=[i for i in range(1,n+1)]

    for x in range(k):
        for y in range(1,n):
            people[y]+=people[y-1]
    print(people[-1])
