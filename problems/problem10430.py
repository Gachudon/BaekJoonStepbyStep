a, b, c = map(int,input().split())
if a>10000 or a<2 or b>10000 or b<2 or c>10000 or c<2:
    quit()
else:
    print((a+b)%c)
    print(((a%c)+(b%c))%c)
    print((a*b)%c)
    print(((a%c)*(b%c))%c)