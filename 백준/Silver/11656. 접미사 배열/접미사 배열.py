s=input().strip()

suff=[s[i:]for i in range(len(s))]
suff.sort()

for suffix in suff:
    print(suffix)