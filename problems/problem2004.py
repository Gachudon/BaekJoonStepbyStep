import sys

def two_count(n:int):
    two=0
    while n != 0:
        n=n//2
        two +=n
    return two

'''
코드 출처: https://tmdrl5779.tistory.com/95
이런식으로 2의 갯수를 구하는 것을 알 수 있었는데...
8!=8*7*6*5*4*3*2*1=> 2가 나오는 횟수는 7번이다.

8=2**3
6=2*3
4=2**2
2=2**1

으로 2가 7번 나온다.
제곱수인 4는 2가 2번
3제곱수인 8은 2가 3번 나오는 것을 알 수 있다.

여기서 알 수 있는 것이 먼저 8! 에서 2의 배수의 갯수를 구한다.
8/2=4
다음으로 제곱수에 대해서 배수를 구한다.
8/(2*2)=2
다음으로 세제곱수에 대해서 배수를 구한다.
8/(2*2*2)=1
즉 4+2+1이란 것이다.
'''

def five_count(n:int): # 5의 배수에 대해서도 앞선 설명을 이용한다.
    five=0
    while n!=0:
        n=n//5
        five+=n
    return five

input=sys.stdin.readline

n, m = map(int, input().split())
print(min(two_count(n) - two_count(n - m) - two_count(m), five_count(n) - five_count(n - m) - five_count(m)))