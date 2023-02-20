a, b, c =map(int,input().split())
price = 0
if a > 6 or a <1 or b > 6 or b <1 or c > 6 or c <1: quit()
if a == b and b == c: price = 10000 + 1000*a
elif a==b: price =1000+100*a
elif b==c: price =1000+100*b
elif c==a: price =1000+100*c
else:
    maximum = max(a,b,c)
    price = 100*maximum
print(price)