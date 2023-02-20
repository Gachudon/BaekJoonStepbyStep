import sys

input=sys.stdin.readline

x=[0]*3
y=[0]*3

for i in range(3):
    x[i],y[i]=map(int,input().split())

w=0
h=0

if x[0]==x[1]:w=x[2]
elif x[1]==x[2]:w=x[0]
elif x[2]==x[0]:w=x[1]

if y[0]==y[1]:h=y[2]
elif y[1]==y[2]:h=y[0]
elif y[2]==y[0]:h=y[1]

print(w,h)

# w=abs(x[0]-x[1])
# if w==0:w=abs(x[0]-x[2])
# h=abs(y[0]-y[1])
# if h==0:h=abs(y[0]-y[2])

# 직사각형을 만들 때 필요한 조건
# 꼭지점의 좌표는 숫자 2가지가 2번씩 들어가야된다.