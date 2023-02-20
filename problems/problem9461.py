d=[0]*101
d[1]=d[2]=d[3]=1
for i in range(4,101):
    d[i]=d[i-2]+d[i-3]

import sys
input=sys.stdin.readline

t=int(input())
n=[0]*t
for i in range(t):
    n[i]=int(input())
    n[i]=d[n[i]]

for i in n:
    print(i)