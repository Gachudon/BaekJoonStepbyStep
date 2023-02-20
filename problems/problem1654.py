'''
코드 출처: https://claude-u.tistory.com/443
이분탐색으로 풀 수 있는 대표적인 알고리즘 문제다.
이분탐색에 대한 정의를 알고 오길 추천한다. (https://claude-u.tistory.com/267)
알고리즘은 쉽다.
랜선의 길이를 움직여 랜선 개수를 채우는 지 보는 것이다.
1) 가장 짧은 길이 1을 start로, 랜선 중 가장 긴 길이를 end로 둔다.
2) 이분탐색이 끝날 때 까지 while 문을 돌린다.

3) mid를 start와 end의 중간으로 두고, 모든 랜선 값을 mid로 나누어 총 몇개의
랜선이 나오나 살펴본다.
4-1) 랜선이 목표치 이상이면 mid+1을 start로 두고 다시 while문 반복
4-2) 랜선이 목표치 이하면 mid-1을 end로 두고 다시 while문 반복
5) start와 end가 같아지면: 조건을 만족하는 최대의 랜선 길이를 찾으면 탈출한다.
6) 결과값인 end 출력
'''

import sys
K,N=map(int,input().split())
lan=[int(sys.stdin.readline()) for _ in range(K)]
start, end=1,max(lan) # 이분탐색 처음과 끝 위치

while start<=end: # 적절한 랜선의 길이를 찾는 알고리즘
    mid=(start+end)//2 # 중간 위치
    lines=0 # 랜선 수
    for i in lan:
        lines += i//mid
    
    if lines>=N:
        start=mid+1
    else:
        end=mid-1

print(end)