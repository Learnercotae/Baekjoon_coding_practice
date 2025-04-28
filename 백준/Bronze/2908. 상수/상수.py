import sys
input=sys.stdin.readline

a,b=map(int,input().split())

c=a//10

d=c%10
e=a//100
f=a%10
sum=(f*100)+(d*10)+e

c_b=b//10

d_b=c_b%10
e_b=b//100
f_b=b%10
sum_b=(f_b*100)+(d_b*10)+e_b

if sum>=sum_b:
    print(sum)
else:
    print(sum_b)
