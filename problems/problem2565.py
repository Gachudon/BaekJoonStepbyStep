'''
코드 출처: https://pacific-ocean.tistory.com/159
우선 2차원 리스트로 입력을 받은 뒤, a전봇대 기준으로 정렬을 하거나, b전봇대
기준으로 정렬을 한다.
위의 코드에선 a전봇대 기준으로 정렬을 하였다. a전봇대 기준으로 정렬을 하면
아래와 같이 리스트가 정렬된다.

1 8
2 2
3 9
4 1
6 4
7 6
9 7
10 10

그럼 b전봇대에서 가장 긴 증가하는 부분수열(11053번)을 구해주면 된다.
1,4,6,7,10 이나 2,4,6,7,10 이 나온다. 교차되어 있는 줄은 총 8개에서 5를 뺀
3개이다.
'''

n=int(input())
w=[]
w_b=[]
dp=[0 for i in range(n)]
for i in range(n):
    w.append(list(map(int,input().split())))
w.sort(key=lambda x:x[0])
for i in range(n):
    w_b.append(w[i][1])
for i in range(n):
    for j in range(i):
        if w_b[i]>w_b[j] and dp[i]<dp[j]:
            dp[i]=dp[j]
    dp[i]+=1
print(n-max(dp))