n=int(input())
if n>1000000 or n<1:quit()
z=list(map(int,input().split()))
if len(z)<n or len(z)>n:quit()
for i in range(n):
    if z[i]>1000000 or z[i]<-1000000:quit()
min=1000000
max=-1000000
for i in range(n):
    if max<z[i]:max=z[i]
    if min>z[i]:min=z[i]
print(min,max)