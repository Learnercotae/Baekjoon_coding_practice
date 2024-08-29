# ex) 256을 2,5,6 으로 나눠서 저장하는 함수 필요

a=int(input())

for i in range(1,a+1):
    num=sum((map(int,str(i)))) # i의 각 자릿수를 더함
    num_sum=i+num # 분해합 = 생성자 + 각 자릿수의 합
    # i가 작은 수부터 차례대로 들어가므로 처음으로 분해합과 입력값이 같을때
    #가장 작은 생성자를 가짐
    if num_sum==a:
        print(i)
        break
    if i==a: #생성자 i와 입력값이 같다는 것은 생성자가 없다는 뜻
        print(0)