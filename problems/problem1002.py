import sys
import math
input=sys.stdin.readline

# x=[0]*2
# y=[0]*2
# r=[0]*2
# ans=[]
# for _ in range(int(input())):
#     x[0],y[0],r[0],x[1],y[1],r[1]=map(int,input().split())

'''
코드 출처: https://ooyoung.tistory.com/111
이 문제는 두 개의 터렛 각각에서 상대편 마린(타겟)까지의 거리가 주어졌을 때,
타깃이 위치할 수 있는 경우의 수를 출력하는 문제이다. 이 문제를 풀 때 두 원의
위치 관계를 이용해서 풀었다. 각 터렛에서 타깃까지의 거리를 토대로 타깃이 위치할
수 있는 점을 조합하면 각 터렛을 중심으로 한 두 개의 원을 그릴 수 있기 때문이다.
두 원의 위치 관계를 이용하기 위해선 두 터렛의 거리가 필요하다. 이 두 터렛의
거리는 원의 방정식을 이용해서 풀었다.
'''

# x1,y1,r1,x2,y2,r2=map(int,input().split())
# distance=math.sqrt((x1-x2)**2+(y1-y2)**2)

'''
터렛 두 개의 좌표(x,y)와 터렛과 타깃까지의 거리(r)를 입력받고서 x1,y1,r1,
x2,y2,r2변수에 선언한다. 두 터렛의 위치가(x,y)좌표로 각각 주어지기 때문에
두 터렛의 거리를 반지름으로 하는 원이 있다고 가정하고서 원의 방정식을 활용해서
두 터렛의 거리를 구했다.
'''

# if distance==0 and r1==r2: # 두 원이 동심원이고 반지름이 같을 때
#     print(-1)
# elif abs(r1-r2)==distance or r1+r2==distance: #내접, 외접일 때
#     print(1)
# elif abs(r1-r2)<distance<(r1+r2): # 두 원이 서로다른 두 점에서 만날 때
#     print(2)
# else:
#     print(0) # 그 외에

'''
각 터렛에서 도출되는 두 원의 접점은 중심거리와 두 원의 위치 관계식을 조건문으로
표현하였다. 위치 관계식을 그대로 보는 게 좋을 것 같아서 중복되는 문장은
단축하지 않았다.

반지름의 길이가 r1인 원과 r2인 원의 중심거리를 d라고 할 때 |r1-r2|또는
r1+r2와 크기를 비교하면, 두 원의 위치 관계를 알 수 있다.

r1+r2<d 이면 두 원은 서로의 외부에 위치한다.
r1+r2=d 이면 두 원은 외접한다.
|r1-r2|<d<r1+r2 이면 두 원은 서로 다른 두 점에서 만난다.
|r1-r2|=d 이면 한 원이 다른 원에 내접한다.
|r1-r2|>d, r1!=r2이면 한 원이 다른 원의 내부에 있다.
'''

n = int(input())
for _ in range(n):
    x1,y1,r1,x2,y2,r2=map(int,input().split())
    distance=math.sqrt((x1-x2)**2+(y1-y2)**2)
    if distance==0 and r1==r2:
        print(-1)
    elif abs(r1-r2) == distance or r1+r2==distance:
        print(1)
    elif abs(r1-r2)<distance<(r1+r2):
        print(2)
    else:
        print(0)