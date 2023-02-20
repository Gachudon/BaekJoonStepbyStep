x=int(input())
if x>1000000000 or x<1:quit()
n=int(input())
if n>100 or n<1:quit()
sum=0
for i in range(n):
    a,b=map(int,input().split())
    if a>1000000 or a<1 or b>10 or b<1: quit()
    sum+=a*b

if sum==x:print('Yes')
else:print('No')