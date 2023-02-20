n=int(input())
arr=list(map(int,input().split()))
arr.sort()
# print(arr)
sumtime=[0]*(n+1)
for i in range(1,n+1):
    sumtime[i]=sumtime[i-1]+arr[i-1]
print(sum(sumtime))