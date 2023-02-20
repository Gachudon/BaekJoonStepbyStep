from sys import stdin

input=stdin.readline
n,m=map(int,input().split())
arr=[None for _ in range(n+1)]
arr[0]=[0 for _ in range(n+1)]
for i in range(1,n+1):
    arr[i]=[0]+list(map(int,input().split()))

# for i in range(n+1):
#     for j in range(n+1):
#         print(arr[i][j],end=' ')
#     print()

# for i in range(1,n):
#     arr[0][i]+=arr[0][i-1]
#     arr[i][0]+=arr[i-1][0]

for i in range(1,n+1):
    for j in range(1,n+1):
        arr[i][j]+=arr[i-1][j]+arr[i][j-1]-arr[i-1][j-1]

# for i in range(n+1):
#     for j in range(n+1):
#         print(arr[i][j],end=' ')
#     print()

ans=[0 for _ in range(m)]
for i in range(m):
    x1,y1,x2,y2=map(int,input().split())
    if x1<=x2:
        xmin=x1
        xmax=x2
    else:
        xmin=x2
        xmax=x1
    if y1<=y2:
        ymin=y1
        ymax=y2
    else:
        ymin=y2
        ymax=y1
    ans[i]=arr[xmax][ymax]-arr[xmax][ymin-1]-arr[xmin-1][ymax]+arr[xmin-1][ymin-1]

for i in ans:
    print(i)