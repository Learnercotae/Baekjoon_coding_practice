
n=input()

if '0' not in n:
    print(-1)
else:
    n_sum=sum(map(int,n))
    if n_sum%3!=0:
        print(-1)
    else:
        result=sorted(n,reverse=True)
        print(''.join(result))
