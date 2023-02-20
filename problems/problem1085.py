import sys

input=sys.stdin.readline

x,y,w,h=map(int,input().split())
min = x
if min>y:min=y
if min>w-x:min=w-x
if min>h-y:min=h-y
print(min)