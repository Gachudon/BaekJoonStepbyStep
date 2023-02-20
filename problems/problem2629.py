'''
코드 출처: https://my-coding-notes.tistory.com/157
양팔 저울을 이용해 주어진 추로 특정 무게를 만드는 문제이다.
주어진 추를 모두 거쳐 무게를 만드는 방법은 3가지가 존재한다.
1. 추의 무게를 더한다.
2. 추의 무게를 뺀다.
3. 추를 사용하지 않는다.

위 3가지 규칙으로 만들 수 있는 모든 무게를 dp에 저장하자.
필자는 보다 쉽게 코드를 작성하기 위해 재귀를 활용했다.
단, 추의 개수가 많아질수록 한 번에 재귀를 3번 호출하는 것은 심각한 성능 문제를
초래하기 마련이다. 따라서 dp를 2차원 배열로 만들어서 추의 개수별로 만들 수 있는
무게 리스트를 만들어 주자.
다음 재귀 때 이미 같은 추의 개수로 똑같은 무게를 만들었다면, 그 다음 과정은
이미 똑같이 밟았을 테니 바로 함수를 return 하면 된다.
'''

n,k = int(input()),list(map(int,input().split()))
m,l = int(input()),list(map(int,input().split()))

# 추의 무게는 최대 500이므로 [[추의 개수*500]*추의 개수]로 배열을 구성한다.
dp,r = [[0 for j in range((i+1)*500+1)] for i in range(n+1)],[]

def cal(num,weight):
    if num > n:
        return 
    
    if dp[num][weight]:
        return
    
    dp[num][weight] = 1
    
    cal(num+1, weight)
    cal(num+1, weight+k[num-1])
    cal(num+1, abs(weight-k[num-1]))
    
cal(0,0)

for i in l:
    if i > 30*500:
        r.append("N")
        continue
    if dp[n][i] == 1:
        r.append("Y")
    else:
        r.append("N")
print(*r)