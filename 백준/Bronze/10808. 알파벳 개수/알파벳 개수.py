n = input()
lst = [0]*26
#lst = [0 for _ in range(26)]


for i in n:
    lst[ord(i)-97] += 1
    #lst[ord(i)-ord('a)] += 1
    
for i in lst:
    print(i, end=' ')