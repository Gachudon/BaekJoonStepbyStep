import sys
input=sys.stdin.readline

n,max_weight=map(int,input().split())

b=[0 for _ in range(n+1)]
w=[0 for _ in range(n+1)]
for i in range(1,n+1):
    w[i],b[i]=map(int,input().split())

bag=[[0 for _ in range(max_weight+1)]for _ in range(n+1)]
for i in range(1,n+1):
    for j in range(1,max_weight+1):
        if w[i] <= j:
            bag[i][j]=max(bag[i-1][j],bag[i-1][j-w[i]]+b[i])
        else:
            bag[i][j]=bag[i-1][j]
print(bag[-1][-1])

# b=[0]*(n+1)
# for i in range(1,n+1):
#     b[i]=tuple(map(int,input().split()))
# bag=[[0]*(k+1)]*n
# for w in range(k+1):
#     bag[0][w]=0
# for i in range(1,n+1):
#     bag[i][0]=0
#     for w in range(1,k+1):
#         if b[i][0] <= w:
#             bag[i][w]=max(bag[i-1][w],bag[i-1][w-b[i][0]]+b[i][1])
#         else:
#             bag[i][w]=bag[i-1][w]
# for i in range(n):
#     for j in range(k):
#         print(bag[i][j],end=' ')
#     print()