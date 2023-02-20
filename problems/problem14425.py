import sys

input=sys.stdin.readline

n,m=map(int,input().split())

a=set()
for _ in range(n):
    a.add(input().replace('\n',''))

# b=set()
# for _ in range(m):
#     b.add(input().replace('\n',''))

# print(len(b.intersection(a)))

cnt=0
for _ in range(m):
    t=input().replace('\n','')
    if t in a:
        cnt+=1
print(cnt)