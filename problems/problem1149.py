'''
첫 번째 집의 색을 정하면 그 다음 집의 색은 최솟값만 정해진다. 라고 가정하고
문제를 풀어보았다.
'''
# import sys
# input=sys.stdin.readline
# n=int(input())
# sum=[0]*3
# r,g,b=map(int,input().split())
# sum[0]=r;sum[1]=g;sum[2]=b
# for _ in range(1,n):
#     rgb=list(map(int,input().split()))
    
'''
코드 출처: https://pacific-ocean.tistory.com/147
0, 1, 2는 각각 빨강, 초록, 파랑을 뜻하고 p[i][0]는 i번째 집을 빨강으로 칠했을
때 최솟값을 나타낸다. p[i][1]과 p[i][2]도 마찬가지로 i번째집을 초록, 파랑으로
칠했을 때의 최솟값을 나타낸다. 이 3개의 값 중에서 가장 작은 값을 출력해주면 된다.
'''

import sys
input=sys.stdin.readline

n=int(input())
p=[None]*n
for i in range(n):
    p[i]=list(map(int,input().split()))

for i in range(1,len(p)):
    p[i][0] = min(p[i-1][1],p[i-1][2])+p[i][0]
    p[i][1] = min(p[i-1][0],p[i-1][2])+p[i][1]
    p[i][2] = min(p[i-1][0],p[i-1][1])+p[i][2]
print(min(p[n-1][0],p[n-1][1],p[n-1][2]))