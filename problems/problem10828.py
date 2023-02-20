from sys import stdin
input=stdin.readline

stack=[]
for _ in range(int(input())):
    c=list(input().split())
    if c[0]=='push':
        stack.append(c[1])
    if c[0]=='pop':
        if len(stack)!=0:
            print(stack.pop())
        else:
            print(-1)
    if c[0]=='size':
        print(len(stack))
    if c[0]=='empty':
        if len(stack)==0:
            print(1)
        else:
            print(0)
    if c[0]=='top':
        if len(stack)!=0:
            print(stack[-1])
        else:
            print(-1)