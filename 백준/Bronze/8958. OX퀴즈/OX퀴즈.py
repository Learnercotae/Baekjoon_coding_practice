a=int(input())


for i in range(a):
    b=input()
    score=0
    sumscore=0
    for j in b:
        if j=='O':
            score += 1
        else:
            score=0
        sumscore += score
    print(sumscore)
                