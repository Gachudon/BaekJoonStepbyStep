'''
마지막 풀이는 두번째 풀이의 원리를 조금 인용해서 소수를 판별하는 가장 효율적인
방법이라고 생각한다. 해당 숫자의 sqrt(N)까지 확인하는 방법이다. 이 원리는
약수의 중심을 구하는 방법이다. 예를 들어 80의 약수는 아래와 같다.

1, 2, 4, 5, 8, 10, 16, 20, 40, 80

각 숫자들의 곱이 80이 되는 쌍을 묶으면 다음과 같다.

1:80, 2:40, 4:20, 5:16, 8:10

sqrt(80)의 값은 8보다 조금 더 큰 값이다. 즉 약수들의 곱으로 봤을 때 루트를
씌운 값이 중간값이 된다. 이 원리를 이용하여 2에서부터 sqrt(N)의 값까지 검색을
한다면 이후의 값은 확인할 필요가 없게 되고 시간복잡도는 O(sqrt(N))이 된다.
'''

# import math

# m,n=map(int,input().split())
# if m>1000000 or m<1 or n>1000000 or n<m:quit()
# for i in range(m,n+1):
#     if i==1:continue
#     elif i==2:
#         print(i)
#         continue
#     isprime=True
#     for j in range(2,int(math.sqrt(i))+1):
#         if i%j==0:isprime=False
#     if isprime:print(i)

'''
코드 출처: https://deokkk9.tistory.com/17
함수를 이용하여 문제를 푸는 것이 빠를 수 있다.
'''

def isPrime(num):
    if num==1:return False
    else:
        for i in range(2,int(num**0.5)+1):
            if num%i==0:
                return False
        return True

m,n=map(int,input().split())
if m>1000000 or m<1 or n>1000000 or n<m:quit()
for i in range(m,n+1):
    if isPrime(i):
        print(i)