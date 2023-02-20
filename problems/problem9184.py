# def w(a:int,b:int,c:int):
#     if a<=0 or b<=0 or c<=0:
#         return 1
#     if a>20 or b>20 or c>20:
#         return w(20,20,20)
#     return

# import sys
# input=sys.stdin.readline
# ans=[]
# while True:
#     a,b,c=map(int,input().split())
#     if a==b==c==-1:break
#     else: ans.append((a,b,c,w(a,b,c)))

'''
내가 생각할 수 있는 부분
초기 값을 모두 0으로 두고, 어떤 조건에 따라 어떤 합차를 구한 뒤, 세 값이
a,b,c가 되도록 한다.

코드 출처: https://jainn.tistory.com/82
첫 번째와 두 번째 if 문을 통해 df의 범위를 정할 수 있다.
0보다 작으면 1로 리턴해 주고, 20보다 크면 w(20,20,20)으로 통일해주기 때문에
dp는 3차원 모두 다 0~20 까지만 초기화시켜놓으면 된다.
그리고 dp값이 존재하면 바로 리턴, 없다면 구하고 리턴하면 된다.
'''

import sys
input = sys.stdin.readline

def w(a, b, c):
    if a <= 0 or b<= 0 or c<=0:
        return 1
    if a > 20 or b > 20 or c > 20:
        return w(20, 20, 20)
    if dp[a][b][c]:
        return dp[a][b][c]
    if a<b<c:
        dp[a][b][c] = w(a,b,c-1)+w(a,b-1,c-1)-w(a, b-1, c)
        return dp[a][b][c]
    dp[a][b][c] = w(a-1, b, c)+w(a-1,b-1,c)+w(a-1,b,c-1)-w(a-1,b-1,c-1)
    return dp[a][b][c]

dp = [[[0]*(21) for _ in range(21)] for _ in range(21)]
# 0~20까지므로

while 1:
    a, b, c = map(int, input().split())
    if a==-1 and b==-1 and c==-1:
        break
    print(f'w({a}, {b}, {c}) = {w(a,b,c)}')