K=int(input())
tup=[]
sum=0

for i in range(K):
    a=int(input())
    if a==0:
        tup.pop()
    else:
        tup.append(a)
for i in tup:
    sum+=i

print(sum)