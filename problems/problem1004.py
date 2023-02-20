import sys
import math
input=sys.stdin.readline

t=int(input())
ans=[None]*t
for i in range(t):
    x1,y1,x2,y2=map(int,input().split())
    n=int(input())
    cnt=0
    for _ in range(n):
        cx,cy,r=map(int,input().split())
        distance1=math.sqrt((x1-cx)**2+(y1-cy)**2)
        distance2=math.sqrt((x2-cx)**2+(y2-cy)**2)
        # if distance1<r or distance2<r and not (distance1<r and distance2<r):
        if distance1<r and distance2>r or distance1>r and distance2<r:
            cnt+=1
    ans[i]=cnt

for i in ans:
    print(i)