# 해시 함수: 임의의 길이의 입력을 받아 고정된 길이의 출력을 내보내는 함수로 정의
# 문자열 영문 소문자 a는 1, b는 2... 처럼 고유한 번호를 부여할 수 있음
# 따라서 하나의 문자열을 수열로 변환할 수 있다.

# 비둘기 집의 원리: 서로 다른 문자열이더라도 동일한 해시 값을 가질 수 있음.
# 이를 해시 충돌이라고 하는데, 최대한 적게 일어나야 함.

# 대표적인 방법: 항의 번호에 해당하는 만큼 특정한 숫자를 거듭제곱해서 곱해준 다음 합.

# 첫 줄: 문자열의 길이 L
# 둘째 줄: 영문 소문자로만 이루어진 문자열

n=int(input())

string=input()

e_sum=0


# 값을 넣을때 alphabet_list값을 알맞게 불러와야 함
for i in range(n):
    char_value=ord(string[i])-96
    e_sum+=char_value*(31**i)

print(e_sum)
