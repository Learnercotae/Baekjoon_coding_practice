#end는 출력 후에 아무 것도 출력하지 않겠다는 의미이며 줄바꿈이 일어나지 않음.
#아래 print()가 대신 줄바꿈을 수행.

a=int(input())

for i in range (1,a+1):
    for j in range(1,i+1):
        print("*",end="")
    print()