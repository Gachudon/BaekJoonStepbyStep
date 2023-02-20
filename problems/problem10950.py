r = int(input())
a=[]
b=[]
for i in range(r):
    c, d = map(int,input().split())
    if c >=10 or c <=0 or d >=10 or d <=0: quit()
    a.append(c)
    b.append(d)

for i in range(r):
    print(a[i]+b[i])