K=int(input())
tup=[]

for i in range(K):
    a=int(input())
    if a==0:
        tup.pop()
    else:
        tup.append(a)

print(sum(tup))