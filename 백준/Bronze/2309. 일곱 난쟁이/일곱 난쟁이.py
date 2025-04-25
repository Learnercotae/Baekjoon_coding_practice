import sys
input=sys.stdin.readline

N=9
ary_N=[]

for i in range(N):
    ary_N.append(int(input()))

ary_sum=sum(ary_N)

found = False
for i in range(N):
    for j in range(i + 1, N):
        if ary_N[i] + ary_N[j] == ary_sum - 100:
            # 두 사람 제거
            a = ary_N[i]
            b = ary_N[j]
            ary_N.remove(a)
            ary_N.remove(b)
            found = True
            break
    if found:
        break


ary_N.sort()
for h in ary_N:
    print(h)
