'''
코드 출처: https://pacific-ocean.tistory.com/153
첫번째 인덱스부터 수열의 길이의 최댓값을 저장해 나간다.
수열 a=[10,20,10,30,20,50]이 있을 때, 4번째 숫자(30)까지의 수열의 길이의
최댓값을 구해보자.
첫번째 숫자부터 검사를 해 나간다. 자기자신(30)보다 작은 숫자들 중 가장 큰
길이를 구하고 그 길이에 +1을 하면 된다.
'''

n=int(input())
a=list(map(int,input().split()))
dp=[0 for i in range(n)]
for i in range(n):
    for j in range(i):
        if a[i]>a[j] and dp[i]<dp[j]:
            dp[i]=dp[j]
    dp[i]+=1
print(max(dp))

# n=int(input())
# a=list(map(int,input().split()))
# dp=[[0] for i in range(n)]
# for i in range(n):
#     for j in range(n):
#         if dp[j][0]==0:
#             dp[j][0]=a[i]
#             break
#         elif dp[j][-1]<a[i]:
#             dp[j].append(a[i])
# max=0
# for i in range(n):
#     if max<len(dp[i]):max=len(dp[i])
# print(max)

# This is ChatGPT's code
# n = int(input())
# a = list(map(int, input().split()))
# dp = [1] * n
# for i in range(n):
#     for j in range(i):
#         if a[j] < a[i]:
#             dp[i] = max(dp[i], dp[j] + 1)
# print(max(dp))
