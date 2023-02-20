a, b, c=map(int,input().split())
if a>2100000000 or a<1 or b>2100000000 or b<1 or c>2100000000 or c<1:quit()
if c<=b:
    print(-1)
    quit()
else:
    p=int(a/(c-b))+1
    print(p)