import math

t=int(input())
r = []
for i in range(t):
    h,w,n=map(int,input().split())
    if h>99 or h<1 or w>99 or w<1 or n>h*w or n<1:quit()
    r.append("%d%02d"%((n-1)%h+1,math.ceil(n/h)))
for i in range(t):
    print(r[i])