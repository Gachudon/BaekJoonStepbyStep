'''
코드 출처: https://jih3508.tistory.com/59
체스판은 2가지 종류가 있다. 맨 위 왼쪽은 검은색일 경우, 흰색일 경우가 있다.
그리고 행+열을 합쳐서 홀 수이면 다른 색 짝수이면 같은 색이라는 것을 알 수 있다.
그 다음에는 위에 2가지 경우와 현재 문제에서 나오는 판이랑 비교해서 차이가 가장
적은 부분을 가져올 생각이다.
'''

from sys import stdin
from sys import maxsize
input=stdin.readline
maxsize

def minimal_board(color):
    prefix_sum=[[0]*(M+1) for _ in range(N+1)]
    for i in range(N):
        for j in range(M):
            if (i+j)%2==0:
                value=board[i][j]!=color
            else:
                value=board[i][j]==color
            prefix_sum[i + 1][j + 1] = prefix_sum[i][j + 1] + prefix_sum[i + 1][j] - prefix_sum[i][j] + value

    count=maxsize
    for i in range(1,N-K+2):
        for j in range(1,M-K+2):
            count = min(count, prefix_sum[i + K - 1][j + K - 1] - prefix_sum[i + K - 1][j - 1] - prefix_sum[i - 1][j + K - 1] + prefix_sum[i - 1][j - 1])
    return count

N,M,K=map(int,input().split())
board=[list(input()) for _ in range(N)]
print(min(minimal_board('B'),minimal_board('W')))