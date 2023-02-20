'''
코드 출처: https://ataraxiady.github.io/dev/2021/04/15/dev-boj-2_11444/
아주아주 큰 수의 피보나치 수를 빠르게 구하는 방법은 바로 행렬의 거듭제곱을
사용하는 것이다.
피보나치가 행렬로도 계산이 되는 지 처음 알았다. 백준님께서 설명해두신 블로그
글을 읽어보면 더 이해가 잘 갈 것 같다.
https://www.acmicpc.net/blog/view/28
'''

import sys
input=sys.stdin.readline
p=1000000007
# 제곱을 구하는 분할정복
def power(adj,n):
    if n==1:
        return adj
    elif n%2:
        return multi(power(adj,n-1),adj)
    else:
        return power(multi(adj,adj),n//2)

# 행렬의 곱셈
def multi(a,b):
    temp=[[0]*len(b[0]) for _ in range(2)]
    for i in range(2):
        for j in range(len(b[0])):
            sum=0
            for k in range(2):
                sum+=a[i][k]*b[k][j]
            temp[i][j]=sum%p
    return temp

# 초기 행렬
adj=[[1,1],[1,0]]
# 피보나치 초기값
start=[[1],[1]]
n=int(input())
if n<3:
    print(1)
else:
    print(multi(power(adj,n-2),start)[0][0])