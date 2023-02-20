a, b = map(int, input().split())
if a>10000 or a <1 or b>10000 or b<1:
    quit()
else:
    print(a+b)
    print(a-b)
    print(a*b)
    print(int(a/b))
    print(a%b)