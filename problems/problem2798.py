import sys
input=sys.stdin.readline

n,m=map(int,input().split())
c=list(map(int,input().split()))
c.sort(reverse=True)
max=0
for i in range(len(c)):
    for j in range(i+1,len(c)):
        for k in range(j+1,len(c)):
            sum = c[i]+c[j]+c[k]
            if sum<=m and max<sum:max=sum

print(max)