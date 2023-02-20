# 코드 출처: https://computer-science-student.tistory.com/676
'''
풀이 출처: https://only-wanna.tistory.com/entry/%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EB%B0%B1%EC%A4%80-10986%EB%B2%88-%EB%82%98%EB%A8%B8%EC%A7%80-%ED%95%A9
미리 구해둔 prefix sum에서 부분 합을 구하려면 p[j]-p[i-1]의 과정을 거쳐야 한다.
이때, p[j]와 p[i-1]이 각각 m으로 나눴을 때의 나머지가 동일하다면 빼기 연산 후
나머지는 0이 돼 M으로 나눠떨어지게 된다.
결국 M으로 나눠떨어지는 부분합을 구하는 것은 나머지가 동일한 idx 중 임의로 nC2를
선택하는 것과 같다.
'''
from sys import stdin

input=stdin.readline
n,m=map(int,input().split()) # n: 숫자 개수, m: 나눌 수
num=list(map(int,input().split()))+[0] # 숫자 입력
r=[0]*m # 누적 합을 m으로 나눴을 때의 나머지가 index이고 그 값에 count

for i in range(n):
    num[i]+=num[i-1] # 숫자 정보를 누적 합으로 갱신
    r[num[i]%m]+=1 # 해당 누적 합을 m으로 나눴을 때의 나머지에 해당하는 값에 1 추가

cnt=r[0] # 연속된 부분 구간의 합이 m으로 나누어 떨어지는 구간의 개수

for i in r:
    cnt+=i*(i-1)//2

print(cnt)

# n,m=map(int,input().split())
# arr=list(map(int,input().split()))

# sum=[0 for _ in range(n+1)]
# for i in range(1,n+1):
#     sum[i]=(sum[i-1]+arr[i-1])

# ans = 0
# for i in range(1,n+1):
#     for j in range(i,n+1):
#         # print(sum[j]-sum[j-i])
#         if (sum[j]-sum[j-i])%m==0:
#             ans+=1

# print(ans)
# for i in range(n):
#     if arr[i]%m==0:ans+=1

# for i in range(n):
#     for j in range(i):
#         if (sum[i]-sum[j])%m==0: