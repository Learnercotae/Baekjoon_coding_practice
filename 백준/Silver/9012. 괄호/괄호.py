T=int(input())

for _ in range(T):
    ps=input()
    stack=[]

    for char in ps:
        if char=='(':
            stack.append(char)
        elif char==')':
            if stack: #스택이 비어있지 않다면
                stack.pop()
            else:
                #스택이 비었는데 닫는 괄호가 나오면
                print("NO")
                break
    else:
        #for문 정상적으로 끝났을 때
        if not stack:
            print("YES")
        else:
            print("NO")