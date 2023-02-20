'''
코드 출처: https://claude-u.tistory.com/449
우리는 이분 탐색으로 어떤 수 보다 작은 자연수의 곱(i*j)이 몇 개인지 알아낼
것이다.
A보다 작은 숫자가 몇개인지 찾아내면 A가 몇 번째 숫자인지 알 수 있다.
예를 들어 10*10에서 20보다 작거나 같은 수를 생각해보자.
1*1~1*10
2*1~2*10
3*1~3*6
...
10*1~10*2
위 수가 존재할 텐데, 이는 반대로 생각해보면 20을 행으로 나눈 몫이다.
20//1: 10개 ->단, 열의 숫자(N*N배열이므로)를 초과할 수 없다.
20//2: 10개
20//3: 6개
...
20//10: 2개
따라서 이를 식으로 표기해보면 아래와 같다.
temp=0
for i in range(1,N+1):
    temp+=min(mid//i,N)

이렇게 해당 숫자(mid)보다 작거나 같은 숫자들을 전부 찾아줌으로써 mid가 몇번째에
위치한 숫자인지 알아낼 수 있다.
'''

N, K = int(input()), int(input())
start, end = 1, K

while start <= end:
    mid = (start + end) // 2
    
    temp = 0
    for i in range(1, N+1):
        temp += min(mid//i, N) #mid 이하의 i의 배수 or 최대 N
    
    if temp >= K: #이분탐색 실행
        answer = mid
        end = mid - 1
    else:
        start = mid + 1
print(answer)

# n=int(input())
# a=[0]*(n*n)
# cnt=0
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         a[cnt]=i*j
#         cnt+=1

# a.sort()

# k=int(input())
# print(a[k-1])