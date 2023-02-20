n,k=map(int,input().split())
arr=list(map(int,input().split()))
sum=[0 for _ in range(n+1)]
for i in range(1,n+1):
    sum[i]=sum[i-1]+arr[i-1]
# print(sum)
subsum=[0 for _ in range(n-k+1)]
for i in range(k,n+1):
    subsum[i-k]=sum[i]-sum[i-k]
    
print(max(subsum))