import sys
input=sys.stdin.readline

cro_list=['c=','c-','dz=','d-','lj','nj','s=','z=']
n=input().strip()

for i in cro_list:
    n=n.replace(i,'*')
print(len(n))