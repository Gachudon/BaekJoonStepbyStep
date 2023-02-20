import sys

input=sys.stdin.readline

n,m=map(int,input().split())
# pokemon=[None]*n
# for i in range(n):
#     pokemon[i]=input().rstrip()
# ans=[None]*m
# for i in range(m):
#     q=input().rstrip()
#     if q.isdigit():
#         ans[i]=pokemon[int(q)-1]
#     else:
#         ans[i]=pokemon.index(q)+1

# for i in ans:
#     print(i)

dict={}
for i in range(1,n+1):
    a=input().rstrip()
    dict[i]=a
    dict[a]=i

for i in range(m):
    quest=input().rstrip()
    if quest.isdigit():
        print(dict[int(quest)])
    else:
        print(dict[quest])