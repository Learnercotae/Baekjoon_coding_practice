# LIFO
# 숫자 '1'부터 'n'까지 오름차순으로 스택에 push하고, 수열 필요할 때마다 스택에서 pop

# 맞을때까지 push, 일치한다면 pop
# 불가능하면 'No' 출력


# 1. 리스트에 1부터 n까지 값을 오른차순으로 집어넣음
# 2. 입력값에 맞게 앞에서부터 하나씩 push
# 3. 일치한다면 pop

count=1
temp=True # 수열을 만들 수 있는지 확인하는 용도
stack=[]
op=[]

n=int(input())

for i in range(n):
    num=int(input())
    
    #num이하 숫자까지 스택에 넣기
    while count<=num:
        stack.append(count)
        op.append('+')
        count+=1

    # num이랑 스택 맨 위 숫자가 같다면 스택에서 제거
    if stack[-1] == num:
        stack.pop()
        op.append('-')
        
    # 스택 수열을 만들 수 없으면 False 후 break
    else:
        temp = False
        break

# 스택 수열을 만들수 있는지 여부에 따라 출력 
if temp == False:
    print("NO")
else:
    for i in op:
        print(i)