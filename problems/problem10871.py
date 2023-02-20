n, x = map(int,input().split())
if n>10000 or n<1 or x>10000 or x<1:quit()
a=list(map(int,input().split()))
if len(a)>n or len(a)<n:quit()
b=[]
for i in range(n):
    if x>a[i]:
        b.append(a[i])
if len(b)<=0:quit()
for i in range(len(b)):print("%d "% b[i],end='')
print()