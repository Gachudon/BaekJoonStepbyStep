n,k=map(int,input().split())
if n>1000 or n<1 or k>n or k<1:quit()
x = list(map(int,input().split()))
if len(x)!=n:quit()
for i in x:
    if i>10000 or i<0:quit()
x.sort(reverse=True)
print(x[k-1])