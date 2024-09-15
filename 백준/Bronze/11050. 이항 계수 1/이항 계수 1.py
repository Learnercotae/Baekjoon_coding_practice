# 자연수 N과 정수 K가 주어졌을때 이항 계수 구하라

# 이항계수: nCp 인듯

a,b=map(int,input().split())
a_sum=1
b_sum=1

for i in range(b):
    a_sum*=(a-i)
    b_sum*=(b-i)
print(a_sum//b_sum)