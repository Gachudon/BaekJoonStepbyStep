import sys

input=sys.stdin.readline

n,m=map(int,input().split())
h=set()
for _ in range(n):
    h.add(input().rstrip())

s=set()
for _ in range(m):
    s.add(input().rstrip())

hs=list(h.intersection(s))
hs.sort()
print(len(hs))
for i in hs:
    print(i)