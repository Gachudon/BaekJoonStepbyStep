import sys
input=sys.stdin.readline

n=int(input())

t=[None]*n
for i in range(n):
    t[i]=list(map(int,input().split()))

for i in range(1,n):
    t[i][0]+=t[i-1][0]
    for j in range(1,len(t[i])-1):
        t[i][j]+=max(t[i-1][j-1],t[i-1][j])
    t[i][-1]+=t[i-1][-1]
max=0
for i in range(len(t[-1])):
    if max<t[-1][i]:max=t[-1][i]
print(max)

# 비슷한 문제: 1149