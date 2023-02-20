t = int(input())
a=[]
b=[]

for i in range(t):
    c,d=map(int,input().split())
    if c>=10 or c<=0 or d>=10 or d<=0:quit()
    a.append(c)
    b.append(d)

for i in range(t):
    print("Case #%d: %d + %d = %d"%(i+1,a[i],b[i],a[i]+b[i]))