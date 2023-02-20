# import sys
# input=sys.stdin.readline

# def isprime(n:int):
#     if n==1: return False
#     for i in range(2,int(n**0.5)+1):
#         if n%i==0:return False
#     return True

# prime_list=[]    
# for i in range(2,10000):
#     if isprime(i):
#         prime_list.append(i)

# n,m=map(int,input().split())
# tmp=n; tmp1=m
# max=1
# while True:
#     if tmp in prime_list or tmp1 in prime_list:
#         break
#     i=0
#     while prime_list[i]<=tmp or prime_list[i]<=tmp1:
#         if tmp%prime_list[i]==0 and tmp1%prime_list[i]==0:
#             max*=prime_list[i]
#             tmp=tmp//prime_list[i]
#             tmp1=tmp1//prime_list[i]
#             break
#         i+=1
# print(max)
# min=max
# while True:
#     if min%n==0 and min%m==0:
#         print(min)
#         break
#     else:
#         min+=max

# 유클리드 호제법을 사용하여 푸는 문제이다.

a,b=map(int,input().split())

def gcd(a,b):
    while b>0:
        a,b=b,a%b
    return a
    
def lcm(a,b):
    return a*b//gcd(a,b)

print(gcd(a,b))
print(lcm(a,b))

# 코드 출처: https://velog.io/@junyp1/%EB%B0%B1%EC%A4%80-2609-Python-%EC%B5%9C%EB%8C%80%EA%B3%B5%EC%95%BD%EC%88%98%EC%99%80-%EC%B5%9C%EC%86%8C%EA%B3%B5%EB%B0%B0%EC%88%98
# 놀라운건 파이썬 math 모듈 속에 이미 최대 공약수와 최소 공배수를 구하는 함수가
# 내장되어 있다는것..
# 참고로 lcm()함수는 파이썬 3.9버전 이상부터 사용 가능하다.