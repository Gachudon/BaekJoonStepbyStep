import sys

input=sys.stdin.readline

# n=int(input())
# # s=[None for _ in range(n)]
# # for i in range(n):
# #     s=list(map(int,input().split()))

# # s=[]
# tmp=[]
# def dfs():
#     # if len(s)==n//2:
#     #     print(' '.join(map(str,s)))
#     #     return
    
#     # for i in range(0,n):
#     #     if i not in s:
#     #         if len(s)==0 or s[-1]<i:
#     #             s.append(i)
#     #             dfs()
#     #             s.pop()
#     global tmp
#     if len(tmp)==n//2:
#         # print(' '.join(map(str,tmp)))
#         tmp1=[]
#         for i in range(n):
#             if i not in tmp:
#                 tmp1.append(i)
#         # compower(tmp)
#         return
    
#     for i in range(0,n):
#         if i not in tmp:
#             if len(tmp)==0 or tmp[-1]<i:
#                 tmp.append(i)
#                 dfs()
#                 tmp.pop()
#             elif tmp[0]>=n//2-1: break

# # tmp2=[]
# # def compower(s:list):
# #     global tmp2
# #     if len(tmp2)==2:
# #         for i in range(2):
            

# dfs()

'''
코드 출처: https://developer-ellen.tistory.com/50
이 문제는 백트래킹(dfs)으로 풀었다.
스타트와 링크 두 팀으로 나누기 위하여 한 팀에 속하면 visited 리스트를 통하여
방문처리 해주면서 재귀함수 형태로 만든다.
만약 한 팀에 속한 팀원의 명수가 n//2로 다 채워졌으면 스타트팀의 능력치와
링크팀의 능력치를 구한다.
방문처리된 팀이 스타트팀이라고 하면, 방문처리 안된 팀이 링크팀이다. 이것을
이용해서 능력치를 구할 수 있다.
두 팀의 능력치 차이의 절대값과 최소 능력치값을 비교하면서 계속 갱신해준다.
'''

def dfs(depth, idx):
    global min_diff
    if depth==n//2:
        power1, power2 = 0, 0
        for i in range(n):
            for j in range(n):
                if visited[i] and visited[j]:
                    power1 += graph[i][j]
                elif not visited[i] and not visited[j]:
                    power2 += graph[i][j]
        min_diff = min(min_diff,abs(power1-power2))
        return
    
    for i in range(idx,n):
        if not visited[i]:
            visited[i]=True
            dfs(depth+1,i+1)
            visited[i]=False

n = int(input())

visited=[False for _ in range(n)]
graph=[list(map(int,input().split())) for _ in range(n)]
min_diff=int(1e9)
dfs(0,0)
print(min_diff)