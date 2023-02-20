def fib(n):
    cnt=1
    if n==1 or n==2:
        return cnt
    else: return fib(n-1)+fib(n-2)

def fibonacci(n):
    cnt=0
    for i in range(2,n):
        cnt+=1
    return cnt

import sys

input=sys.stdin.readline

n=int(input())
print(fib(n),fibonacci(n))