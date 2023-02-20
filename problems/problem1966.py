# 참조: https://hellominchan.tistory.com/156

from sys import stdin
from collections import deque
input=stdin.readline

t=int(input())
ans=[0]*t
for i in range(t):
    n,m=map(int,input().split())
    queue=deque(map(int,input().split()))
    while len(queue)>0:
        if queue[0]<max(queue):
            queue.append(queue.popleft())
            m-=1
            if m<0:m=len(queue)-1
        else:
            queue.popleft()
            ans[i]+=1
            m-=1
            if m<0:break

for i in ans:
    print(i)