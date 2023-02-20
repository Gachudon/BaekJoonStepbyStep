from sys import stdin
input=stdin.readline

n,k=map(int,input().split())
a=[0]*n
for i in range(n):
    a[i]=int(input())
count=0
while k>0:
    for i in range(n-1,-1,-1):
        # print(i)
        if k>=a[i]:
            tmp=k//a[i]
            count+=tmp
            k=k-tmp*a[i]
            break
print(count)

# for i in range(n-1,-1,-1):
#     print(a[i])