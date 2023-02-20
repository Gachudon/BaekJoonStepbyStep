'''
코드 출처: https://rhdtka21.tistory.com/123
풀이가 난해함으로 직접 접속해서 확인해보세요.
'''

import sys
read = sys.stdin.readline

def power(a,b):
    if b==0:
        return 1
    if b%2:
        return (power(a,b//2)**2*a)%p
    else:
        return (power(a,b//2)**2)%p
    
p=1000000007

N,K=map(int,read().split())

fact=[1 for _ in range(N+1)]

for i in range(2,N+1):
    fact[i]=fact[i-1]*i%p

A=fact[N]
B=(fact[N-K]*fact[K])%p

print((A%p)*(power(B,p-2)%p)%p)

# from math import comb

# n,k=map(int,input().split())

# print(comb(n,k)%1000000007)