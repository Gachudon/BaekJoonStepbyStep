# n=int(input())
# a=list(map(int,input().split()))
# dp=[1]*n
# for i in range(n):
#     for j in range(i):
#         if a[j]<a[i]:
#             dp[i]=max(dp[i],dp[j]+1)
#         # elif a[j]>a[i]:
#         #     dp[i]=max(dp[i],dp[j]+1)
# print(max(dp))

# This is ChatGPT's code

n = int(input())
a = list(map(int, input().split()))

inc = [1 for i in range(n)]
dec = [1 for i in range(n)]

for i in range(1, n):
    for j in range(i):
        if a[i] > a[j] and inc[i] < inc[j] + 1:
            inc[i] = inc[j] + 1

for i in range(n - 2, -1, -1):
    for j in range(n - 1, i, -1):
        if a[i] > a[j] and dec[i] < dec[j] + 1:
            dec[i] = dec[j] + 1

max_len = 0
for i in range(n):
    max_len = max(max_len, inc[i] + dec[i] - 1)

print(max_len)
