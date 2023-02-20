import sys
input=sys.stdin.readline

an,bn=map(int,input().split())

a=set(map(int,input().split()))
b=set(map(int,input().split()))

s=a^b
print(len(s))