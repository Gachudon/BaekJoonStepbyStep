import sys
input=sys.stdin.readline

n=int(input())

a=list(map(int,input().split()))

max=a[0]
min=a[0]
for i in a:
    if max<i:max=i
    if min>i:min=i
print(max*min)