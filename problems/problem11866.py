'''
코드 출처: https://pacific-ocean.tistory.com/233
입력받은 k번째까지 요소를 없애고, 그 요소들을 뒤에 추가해 준다.
k번째 숫자를 출력해주고 그 요소를 없애준다.
요소가 없어질 때 까지 반복해준다.
'''
from collections import deque
n,k=map(int,input().split())
s=deque([])
for i in range(1,n+1):
    s.append(i)
print('<',end='')
while s:
    for i in range(k-1):
        s.append(s[0])
        s.popleft()
    print(s.popleft(),end='')
    if s:
        print(', ',end='')
print('>')