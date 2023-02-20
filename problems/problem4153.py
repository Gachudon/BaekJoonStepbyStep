import sys
input=sys.stdin.readline

def isRT(a,b,c):
    if c**2==a**2+b**2 or b**2==a**2+c**2 or a**2==b**2+c**2:
        return 'right'
    return 'wrong'

ans=[]
while True:
    a,b,c=map(int,input().split())
    if a==b==c==0:break
    ans.append(isRT(a,b,c))

for i in ans:
    print(i)