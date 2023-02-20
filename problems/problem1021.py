from collections import deque

n,m=map(int,input().split())
data=list(map(int,input().split()))

dq=deque([i for i in range(1,n+1)])
ans=0

for d in data:
    if dq.index(d) > len(dq)//2:
        while dq[0]!=d:
            dq.appendleft(dq.pop())
            ans+=1
        dq.popleft()
    else:
        while dq[0]!=d:
            dq.append(dq.popleft())
            ans+=1
        dq.popleft()
print(ans)