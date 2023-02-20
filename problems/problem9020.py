# def isPrime(num):
#     if num==1:return False
#     else:
#         for i in range(2,int(num**0.5)+1):
#             if num%i==0:
#                 return False
#         return True

# prime_num=[]

# for i in range(1,10001):
#     if isPrime(i):prime_num.append(i)

# # print(len(prime_num))

# t=int(input())
# gb=[]
# for i in range(t):
#     n=int(input())
#     if n>10000 or n<4 or n%2!=0:quit()
#     j=0
#     tmp=[]
#     while prime_num[j]<=int(n/2):
#         m=n-prime_num[j]
#         if m in prime_num:
#             tmp=[prime_num[j],m]
#         j+=1
#     gb.append(tmp)

# for i in gb:
#     print("%d %d"%(i[0],i[1]))

'''
코드 출처: https://velog.io/@jieuihong/%EB%B0%B1%EC%A4%80-9020-%EA%B3%A8%EB%93%9C%EB%B0%94%ED%9D%90%EC%9D%98-%EC%B6%94%EC%B8%A1%EC%8B%A4%EB%B2%841-Python
처음에는 너무 복잡하게 생각해서 num 이하의 소수를 따로 리스트에 넣어서
그 수들의 조합을 구해서 그 조합들의 숫자들이 더해서 num이 되는지를 확인하고
그 중에서 또 차이가 더 적은 한 쌍을 구하는 코드를 짰는데 역시나 시간 초과ㅋ

구글링을 해봤더니 너무나도 간단한 답이 있었다.
num을 반으로 쪼개고 한 개는 +1씩, 한 개는 -1씩 해보면서 두 수가 모두 소수인지
확인하는 것.
'''

def is_prime(n):
    if n == 1:
        return False
    for j in range(2, int(n**0.5) + 1):
        if n % j == 0:
            return False
    return True


for _ in range(int(input())):
    num = int(input())

    a, b = num//2, num//2
    while a > 0:
        if is_prime(a) and is_prime(b):
            print(a, b)
            break
        else:
            a -= 1
            b += 1