import sys
input=sys.stdin.readline
a=[]
sum=0

for i in range(5):
    a.append(int(input()))
    sum+=a[i]

sum_a=sum//5
a.sort()
middle=a[2]

print(sum_a)
print(middle)