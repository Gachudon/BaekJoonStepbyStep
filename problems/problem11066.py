'''
https://blue-coding-story.tistory.com/131
'''

def solution():
    n=int(input())
    data=[0]+list(map(int,input().split()))
    #s는 누적합
    s=[0 for _ in range(n+1)] # 누적합 리스트
    for i in range(1,n+1):
        s[i]=s[i-1]+data[i]
    
    dp=[[0 for _ in range(n+1)] for _ in range(n+1)]
    for i in range(2,n+1):
        for j in range(1,n+2-i): # 시작 (i-j)
            dp[j][j+i-1]=min([dp[j][j+k]+dp[j+k+1][j+i-1] for k in range(i-1)]) + (s[j+i-1] - s[j-1])

    print(dp[1][n])

for _ in range(int(input())):
    solution()
# from sys import stdin
# input=stdin.readline

# t=int(input())
# ans=[0]*t
# for i in range(t):
#     k=int(input())
#     c=list(map(int,input().split()))