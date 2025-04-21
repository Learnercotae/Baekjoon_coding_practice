N=int(input())

sum=[]
for i in range(N):
    a,b=map(int,input().split())
    sum.append([a,b])

sum.sort(key=lambda x: (x[0],x[1])) 

for i in range(N):
    print(sum[i][0],sum[i][1])