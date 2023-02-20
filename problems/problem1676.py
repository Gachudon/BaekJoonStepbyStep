import sys
from math import factorial

input=sys.stdin.readline

n=int(input())

n=factorial(n)
# for i in str(n):
ans=0
for i in reversed(str(n)):
    if i=='0':
        ans+=1
    else: break

print(ans)