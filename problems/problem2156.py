import sys
input=sys.stdin.readline

n=int(input())
w=[0]*(n+1)
for i in range(1,n+1):
    w[i]=int(input())
dp=[0]*(n+1)
dp[1]=w[1]
if n> 1:
    dp[2]=w[1]+w[2]
for i in range(3,n+1):
    dp[i]=max(dp[i-1],dp[i-3]+w[i-1]+w[i],dp[i-2]+w[i])
print(dp[n])

'''
코드 출처: https://pacific-ocean.tistory.com/152
첫 번째로 해당 순서의 포도주를 마시는 경우, 그 전 포도주를 안 먹는 경우와 먹는
경우가 있다. w가 포도주양을 담은 리스트라고 할 떄,
dp[3]의 경우의 수에서 w1+w2는 dp[2]와 같다.
dp[4]의 경우의 수에서 w2+w3는 dp[3]이고, w1+w2+w4에서 w1+w2는 dp[2]이다.
그리고 w1+w3+w4에서 w1은 dp[1]이다. 그래서 식을 세워보자면,
dp[4]의 경우의 수: dp[4-1],dp[4-3]+w[4-1]+w[4],dp[4-2]+w[4]
4를 i로 바꿨을 때,
dp[i-1],dp[i-3]+w[i-1]+w[i],dp[i-2]+w[i]이 세가지 값 중 가장 큰 값을 넣어주면
된다.
'''

# n=int(input())
# v=[0]*n
# dp=[0]*n
# for i in range(0,n):
#     v[i]=int(input())

# dp[0]=v[0]
# dp[1]=v[0]+v[1]
# dp[2]=max(v[1]+v[2],v[0]+v[2])

# for i in range(3,n):
#     dp[i]=max(dp[i-3]+v[i-1]+v[i],dp[i-2]+v[i])
# print(max(dp))