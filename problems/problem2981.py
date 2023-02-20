# n=int(input())
# num_list=[0]*n
# max=0
# for i in range(n):
#     num_list[i]=int(input())
#     if max<num_list[i]:max=num_list[i]

# for i in range(2,max+1):
#     rest_set=set()
#     for j in num_list:

'''
코드 출처: https://tmdrl5779.tistory.com/94
수학적 이론이 필요한 문제이다.
M을 찾아야 한다.

A=M*a+R
B=M*b+R
C=M*c+R

여기서 R을 제거하면

A-B=M(a-b)
B-C=M(b-c)

이런 식이 나온다.
즉,
M은 A-B, B-C의 공약수이다 즉 최대 공약수를 구하면 된다.
최대 공약수를 구하고 해당 수의 1을 제외한 약수를 출력하면 된다.

이때 최대 공약수를 구하고 약수를 구할 때 반복문을 최대공약수 까지 돌려버리면
숫자 범위가 1,000,000,000까지기 때문에 엄청난 시간이 걸린다.

그래서 공약수를 구할 때
18%2=0(2=약수)
18//2=9 (9=약수)
이 2개를 한번에 구한다. 이러면 반복횟수를 최대 공약수의 제곱근 까지
줄일 수 있다.
마지막에 자기 자신도 추가한다.
'''
import sys
from math import gcd
from math import sqrt

input=sys.stdin.readline

n = int(input())
ns = list(int(input()) for _ in range(n))
ns.sort()
interval=list()
ans=list()

for i in range(1,n):
    interval.append(ns[i]-ns[i-1])

prev=interval[0]
for i in range(1,len(interval)):
    prev=gcd(prev,interval[i])

for i in range(2,int(sqrt(prev))+1):
    if prev%i==0:
        ans.append(i)
        ans.append(prev//i)
ans.append(prev)
ans = list(set(ans))
ans.sort()
print(*ans)