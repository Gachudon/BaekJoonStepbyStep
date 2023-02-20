import sys
from math import factorial

def binomialcoefficient(n:int,k:int):
    return factorial(n)//factorial(k)//factorial(n-k)

input=sys.stdin.readline

n,k=map(int,input().split())

print(binomialcoefficient(n,k)%10007)