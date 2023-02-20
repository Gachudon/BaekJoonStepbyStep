import sys
from math import gcd
input=sys.stdin.readline

n=int(input())
ring_list=list(map(int,input().split()))

for i in range(1,n):
    tmp = gcd(ring_list[0],ring_list[i])
    print("%d/%d"%(ring_list[0]//tmp,ring_list[i]//tmp))