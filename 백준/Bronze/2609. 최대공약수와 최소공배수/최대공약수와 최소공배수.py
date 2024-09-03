# 두 개의 자연수를 입력받음
# 최대 공약수와 최소 공배수 출력


# 유클리드 호제법 사용하여 푸는 문제

a,b=map(int,input().split())

def gcd(a,b):
    while b>0:
        a,b= b,a%b
    return a

def lcm(a,b):
    return a*b //gcd(a,b) # '/'일 경우에는 실수 반환, '//'일 경우 정수 반

print(gcd(a,b))
print(lcm(a,b))