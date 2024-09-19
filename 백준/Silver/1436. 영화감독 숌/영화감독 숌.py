n=int(input())
count=0
fate=666

while True:
    if '666' in str(fate):
        count+=1
    if count ==n:
        break
    fate+=1

print(fate)
