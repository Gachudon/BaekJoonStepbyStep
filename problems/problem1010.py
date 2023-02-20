import sys
from math import factorial

def binomialcoefficient(n:int,k:int):
    return factorial(n)//factorial(k)//factorial(n-k)

input=sys.stdin.readline

t=int(input())
ans=[0]*t
for i in range(t):
    n,k=map(int,input().split())
    ans[i]=binomialcoefficient(k,n)

for i in ans:
    print(i)