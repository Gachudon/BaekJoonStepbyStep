import sys
input=sys.stdin.readline
ans=[]
while True:
    n,m=map(int,input().split())
    if n==0 and m==0:break
    if m%n==0:ans.append("factor")
    elif n%m==0:ans.append("multiple")
    else:ans.append("neither")

for i in ans:
    print(i)