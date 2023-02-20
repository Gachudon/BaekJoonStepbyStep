n=int(input())
if n>100 or n<1:quit()
z=list(map(int,input().split()))
if len(z)>n or len(z)<n:quit()
for i in range(n):
    if z[i]>100 or z[i]<-100:quit()
v=int(input())
if v>100 or v<-100:quit()
cnt=0
for i in range(n):
    if z[i]==v:cnt+=1
print(cnt)