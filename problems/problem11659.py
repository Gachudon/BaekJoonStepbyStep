# 풀이 출처: https://jow1025.tistory.com/47

from sys import stdin
input=stdin.readline

n,m=map(int,input().split())
arr=list(map(int,input().split()))
sum=[0 for _ in range(n+1)]
sum[0]=0
sum[1]=arr[0]
for k in range(2,n+1):
    sum[k]=sum[k-1]+arr[k-1]
ans=[0 for _ in range(m)]
for k in range(m):
    i,j=map(int,input().split())
    # for p in range(i-1,j):
    #     sum[k]+=arr[p]
    ans[k]=sum[j]-sum[i-1]
for k in ans:
    print(k)
# because of commit mistake, this line is added to fix it