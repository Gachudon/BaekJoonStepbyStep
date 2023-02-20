'''
코드 출처: https://hongcoding.tistory.com/44
이 문제는 입력을 특이하게 괄호와 쉼표를 모두 포함하여 받는다.
[1:-1]범위의 부분만 가져와서 deque를 만들어 준다.
Reverse를 해야 할 때 마다 매번 deque를 뒤집어 주어야 하기 때문에 뒤집는 횟수가
홀수 번 일 때만 뒤집도록 수정하였다.
'''

from sys import stdin
from collections import deque
input=stdin.readline

t=int(input())
for i in range(t):
    p=input().rstrip()
    n=int(input())
    arr=input().rstrip()[1:-1].split(',')
    queue=deque(arr)

    rev,front,back=0,0,len(queue)-1
    flag=0
    if n==0:
        queue=[]
        front=0
        back=0

    for j in p:
        if j=='R':
            rev+=1
        elif j=='D':
            if len(queue)<1:
                flag=1
                print('error')
                break
            else:
                if rev%2==0:
                    queue.popleft()
                else:
                    queue.pop()
    if flag==0:
        if rev%2==0:
            print("["+",".join(queue)+"]")
        else:
            queue.reverse()
            print("["+",".join(queue)+"]")

# from sys import stdin
# from collections import deque

# input=stdin.readline

# t=int(input())
# ans=[None]*t

# for i in range(t):
#     p=input().rstrip()
#     n=int(input())
#     x=input().rstrip()
#     if x=='[]':
#         ans[i]='error'
#         continue
#     x=deque(map(int,x[1:-1].split(',')))
#     r=0
#     for j in p:
#         if j=='R':
#             r+=1
#         elif j=='D' and r%2==0:
#             if len(x)>0:
#                 x.popleft()
#             else:
#                 ans[i]='error'
#                 break
#         elif j=='D' and r%2==1:
#             if len(x)>0:
#                 x.reverse()
#                 r=0
#                 x.popleft()
#             else:
#                 ans[i]='error'
#                 break
    
#     if ans[i]!=None:continue
#     else:ans[i]=list(x)

# for i in ans:
#     print(i)