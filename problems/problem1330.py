a, b = map(int,input().split())
if a >10000 or a <-10000 or b >10000 or b <-10000:
    quit()
elif a>b:
    print(">")
elif a<b:
    print("<")
else:
    print("==")