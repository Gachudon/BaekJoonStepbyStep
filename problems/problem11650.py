import sys

n=int(sys.stdin.readline())
p=[None]*n
for i in range(n):
    p[i]=tuple(map(int,input().split()))
    if p[i][0]>100000 or p[i][0]<-100000 or p[i][1]>100000 or p[i][1]<-100000:quit()

p=sorted(p,key=lambda x:x[1])
p=sorted(p,key=lambda x:x[0])
for i in p:
    print(i[0],i[1])