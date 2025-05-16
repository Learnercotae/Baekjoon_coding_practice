import sys
input=sys.stdin.readline

n=int(input())

#딕셔너리 활용
arr={}


for i in range(n):
    book=input().strip()
    if book in arr:
        arr[book]+=1
    else:
        arr[book]=1

#values 활용
max_count=max(arr.values())

#items 활용
best_sellers=[book for book, count in arr.items() if count==max_count]
best_sellers.sort()

print(best_sellers[0])