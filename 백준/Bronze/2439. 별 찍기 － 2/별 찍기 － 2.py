#*개수는 1과 동일하게 늘어나지만, 출력이 문장 끝에서부터 된다는 점이 다름.
# 컴코때 배웠던거 같음..

a=int(input())

for i in range (1,a+1):
    print(" "*(a-i)+"*"*i)