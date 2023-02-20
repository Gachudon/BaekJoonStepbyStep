'''
코드 출처: https://pacific-ocean.tistory.com/228
최솟값을 만들기 위해서는 '-' 기준으로 괄호를 치면 된다.
'''

a = input().split('-')
num = []
for i in a:
    cnt = 0
    s = i.split('+')
    for j in s:
        cnt += int(j)
    num.append(cnt)
n = num[0]
for i in range(1, len(num)):
    n -= num[i]
print(n)