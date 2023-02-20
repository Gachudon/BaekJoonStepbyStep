'''
코드 출처: https://studyandwrite.tistory.com/387
DFS+DP를 이용한 문제입니다.
우선 이 문제를 DFS로만 풀려면 가능한 모든 경로의 수를 다 세야하기 때문에 정말
많은 경우의 수가 나오게 됩니다. 그러면 시간초과가 뜨겠죠? 500*500 배열에서
계속해서 상하좌우로 이동이 가능한 상황을 떠올려보면 직관적으로 느낄 수 있습니다.

따라서 이 문제는 DP를 이용해서 불필요한 연산을 출여야 하는데, 이를 위해서는
우선 DP의 사용 정당성에 대해 고민해봐야 합니다. 즉, 전체 문제의 최적해가
부분 문제의 최적해로 쪼개질 수 있는가? 를 입증해야 하는 것이죠.

이 문제의 경우 시작, 도착점이 아닌 임이의 지점(a,b)에서 도착지점 (m-1,n-1)까지
가는 경우의 수가 구해지면, 그 이전의 어떤 경로로(a,b)에 도착하기만 하면
그 때부터의 경우의 수는 다시 구할 필요가 없습니다.

다시 말해서, 도착 지점까지 가는 경우의 수는 도착지점이 아닌 임의의 점들에서도
도착지점까지 가는 경우의 수를 합한 것과 같아진다는 것이죠.

그렇다면 다음으로는 어떻게 메모이제이션을 할 것인가? 에 대한 물음이 남습니다.
저는 대부분의 DP 문제를 bottom-up 방식으로 푸는 데 익숙하기 때문에 이 문제도
같은 방식으로 해결했습니다.

시작 지점에서 출발해서 DP 테이블이 갱신되지 않은 곳(X)을 만난다면, 해당 지점(X)
부터 도착 지점까지 갈 수 있는 경로의 수를 그곳에 업데이트 합니다. X지점의 DP
테이블이 이미 갱신되어 있다면 그 곳이 위에서 말한 부분 최적해가 되므로 그 값을
그대로 전체 정답에 더해주면 됩니다.
'''
import sys
sys.setrecursionlimit(10**8)
input=sys.stdin.readline

def dfs(sx,sy):
    # 도착 지점에 도달하면 1(한 가지 경우의 수)를 리턴
    if sx==m-1 and sy==n-1:
        return 1
    
    # 이미 방문한 적이 있다면 그 위치에서 출발하는 경우의 수를 리턴
    if dp[sx][sy]!=-1:
        return dp[sx][sy]
    
    ways=0
    for i in range(4):
        nx,ny=sx+dx[i],sy+dy[i]
        if 0<=nx<m and 0<=ny<n and graph[sx][sy]>graph[nx][ny]:
            ways+=dfs(nx,ny)

    dp[sx][sy]=ways
    return dp[sx][sy]

m,n=map(int,input().split())
graph=[list(map(int,input().split())) for _ in range(m)]
dp=[[-1]*n for _ in range(m)]
dx,dy=[1,-1,0,0],[0,0,1,-1]

print(dfs(0,0))