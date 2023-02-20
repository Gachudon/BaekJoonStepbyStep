from sys import stdin
input=stdin.readline
n=int(input())
queue=[0]*n
front=0
back=1
for _ in range(n):
    c=list(input().split())
    if c[0]=='push':
        queue[back]=c[1]
        back=(back+1)%n
    elif c[0]=='pop':
        if back-front!=1:
            print(queue[(front+1)%n])
            front=(front+1)%n
        else:
            print(-1)
    elif c[0]=='size':
        print(back-front-1)
    elif c[0]=='empty':
        if back-front==1:
            print(1)
        else:
            print(0)
    elif c[0]=='front':
        if back-front!=1:
            print(queue[front+1])
        else:
            print(-1)
    elif c[0]=='back':
        if back-front!=1:
            print(queue[back-1])
        else:
            print(-1)

# from sys import stdin
# import queue
# input=stdin.readline

# q=queue.Queue()
# for _ in range(int(input())):
#     c=list(input().split())
#     if c[0]=='push':
#         q.put_nowait(c[1])
#     if c[0]=='pop':
#         if q.qsize()!=0:
#             print(q.get_nowait())
#         else:
#             print(-1)
#     if c[0]=='size':
#         print(q.qsize())
#     if c[0]=='empty':
#         if q.qsize()==0:
#             print(1)
#         else:
#             print(0)
#     if c[0]=='front':
#         if q.qsize()!=0:
#             print(list(q.queue)[0])
#         else:
#             print(-1)
#     if c[0]=='back':
#         if q.qsize()!=0:
#             print(list(q.queue)[-1])
#         else:
#             print(-1)