# 피보나치 함수

# 재귀로는 시간초과
# 따라서 DP활용

# 피보나치 DP 설정
def count_fibonacci(n):
    #[0]은 필요 없으므로 n+1까지 생성
    #하나는 0 카운트, 하나는 1 카운트
    count_zeros=[0] * (n+1)
    count_ones=[0] * (n+1)

    # 만약 n이 0보다 크다면
    if n>=0:
        #zeros[0]에 1을 넣음으로 왔다감을 표시
        count_zeros[0]=1
        #ones[0]은 0이므로 1이 없음을 표시
        count_ones[0]=0
    if n>=1:
        #zeros[1]에 0을 넣음으로 없음을 표시
        count_zeros[1]=0
        #ones[1]에 1을 넣음으로 왔다감을 푯
        count_ones[1]=1

    #0과 1을 제외한 다음 숫자들 계산
    for i in range(2,n+1):
        #피보나치 수열
        count_zeros[i]=count_zeros[i-1]+count_zeros[i-2]
        count_ones[i]=count_ones[i-1]+count_ones[i-2]

    return count_zeros[n],count_ones[n]

T=int(input())

for i in range(T):
    x=int(input())
    zero_count,one_count=count_fibonacci(x)
    print(zero_count,one_count)