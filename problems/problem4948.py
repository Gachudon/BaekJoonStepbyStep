# def isPrime(num):
#     if num==1:return False
#     else:
#         for i in range(2,int(num**0.5)+1):
#             if num%i==0:
#                 return False
#         return True

# b=[]
# while True:
#     n=int(input())
#     if n==0:break
#     elif n>123456 or n<1:quit()
#     cnt=0
#     for i in range(n+1,2*n+1):
#         if isPrime(i):cnt+=1
#     b.append(cnt)

# for i in b:print(i)

'''
코드 출처:https://velog.io/@iillyy/%EB%B0%B1%EC%A4%80-4948%EB%B2%88-%ED%8C%8C%EC%9D%B4%EC%8D%AC
처음에는 이런 식으로 모든 소수를 구하고 입력받은 n값 안에서의 소수를 찾게
했는데 시간 초과가 떴습니다. 크게 손보지 않는 한에서 해결방안은 모든 소수가
아닌 문제에서 제한한 범위 1<=n<=123,456 안에서 소수만 저장하고 for문을
돌리는 동안 소수 리스트에 있는 소수들을 꺼내오는 방식으로 풀었습니다.
'''
def sosu(n):
    if n ==1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True							#소수 구하는 방식은 위와 같다

all_list = list(range(2,246912))		#문제에서 제한한 범위
memo = []								#for문 밖에 리스트 정의

for i in all_list:						#2부터 2*123,456 범위
    if sosu(i):							#sosu함수에 해당하면
        memo.append(i)					#리스트에 추가

n = int(input())

while True:
    count=0					#갯수를 세야하는 조건 때문에 카운트
    if n == 0 :
            break
    for i in memo:			#memo리스트 중에서
        if n < i <=2*n:		#입력한 값의 범위 내에서 값이 있으면
            count+=1		#있을 때 마다 카운트 +1
    print(count)
    n = int(input())		#0 입력받기 전까지 계속 해야하므로 입력 받음