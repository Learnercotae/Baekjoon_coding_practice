# 자기 점수 중에 최댓값 M을 고름.
# 그리고 나서 모든 점수를 점수/M*100으로 고침

# 첫째 줄: 시험 본 과목의 개수 N
# 둘째 줄: 현재 성적


n=int(input())
scores=list(map(int,input().split()))

max_score=max(scores)

# scores 리스트에 있는 각 정수를 하나씩 가져와 score 변수에 할당
# 각 socre에 대해 계산 수행
# 결과값을 new_scores리스트에 순서대로 추가

new_scores=[(score/max_score)*100 for score in scores] # 컴프리헨션 문법 사용
average=sum(new_scores)/n

print(average)
