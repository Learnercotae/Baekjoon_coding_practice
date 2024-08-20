# while문 활용해야 된다는걸 바로 생각나게끔 연습 필요.
# 마지막 입력 0 0 0을 받으면 입력이 마무리 되니까 당연히 while문 필요

while True:
    nums=list(map(int,input().split()))
    if sum(nums)==0:
        break
    nums.sort()
    if nums[0]**2 + nums[1]**2==nums[2]**2:
        print('right')
    else:
        print('wrong')
