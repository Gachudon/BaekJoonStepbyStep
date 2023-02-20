import heapq
from sys import stdin
input=stdin.readline

n=int(input())
heap=[]

for _ in range(n):
    num=int(input())
    if num==0:
        try:
            print(-1*heapq.heappop(heap))
        except:
            print(0)
    else:
        heapq.heappush(heap,-num)