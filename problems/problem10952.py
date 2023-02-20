a=[]
b=[]

while True:
    c,d=map(int,input().split())
    if c>=10 or c<0 or d>=10 or d<0:quit()
    elif c==0 and d==0:break
    elif c==0 or d==0:quit()
    a.append(c)
    b.append(d)

for i in range(len(a)): print(a[i]+b[i])