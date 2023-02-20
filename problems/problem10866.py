from sys import stdin
from collections import deque
input=stdin.readline

dq=deque([])
for _ in range(int(input())):
    c=list(input().split())
    if c[0]=='push_front':
        dq.appendleft(c[1])
    elif c[0]=='push_back':
        dq.append(c[1])
    elif c[0]=='pop_front':
        if len(dq)>0:
            print(dq.popleft())
        else:
            print(-1)
    elif c[0]=='pop_back':
        if len(dq)>0:
            print(dq.pop())
        else:
            print(-1)
    elif c[0]=='size':
        print(len(dq))
    elif c[0]=='empty':
        if len(dq)!=0:
            print(0)
        else:
            print(1)
    elif c[0]=='front':
        if len(dq)>0:
            print(dq[0])
        else:
            print(-1)
    elif c[0]=='back':
        if len(dq)>0:
            print(dq[-1])
        else:
            print(-1)