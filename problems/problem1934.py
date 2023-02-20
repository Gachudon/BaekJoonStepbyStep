import sys
input=sys.stdin.readline

# a,b=map(int,input().split())

def gcd(a,b):
    while b>0:
        a,b=b,a%b
    return a
    
def lcm(a,b):
    return a*b//gcd(a,b)

# print(gcd(a,b))
# print(lcm(a,b))

t=int(input())
ans=[0]*t
for i in range(t):
    a,b=map(int,input().split())
    ans[i]=lcm(a,b)

for i in ans:
    print(i)