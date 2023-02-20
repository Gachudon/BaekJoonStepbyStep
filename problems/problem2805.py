'''
코드출처: https://claude-u.tistory.com/446
벌목 높이를 움직여 필요 나무 길이를 채우는 지 보는 것이다.
1) 가장 짧은 길이 1을 start로, 나무 중 가장 긴 길이를 end로 둔다.
2) 이분탐색이 끝날 때 까지 while 문을 돌린다.

3) mid를 start와 end의 중간으로 두고, 모든 값에서 mid를 빼 총 어느정도 길이의
벌목된 나무가 나오나 살펴본다.
4-1) 벌목나무가 목표치 이상이면 mid+1을 start로 두고 다시 while문 반복
4-2) 벌목나무가 목표치 이하면 mid-1을 end로 두고 다시 while문 반복
5)start와 end가 같아지면: 조건을 만족하는 최대의 나무 절단 높이를 찾으면
탈출한다.
6)결과값인 end 출력
'''

n,m=map(int,input().split())
tree=list(map(int,input().split()))
start, end=1,max(tree)

while start <=end:
    mid = (start+end)//2
    cut=0
    for i in tree:
        if mid<=i:
            cut+=i-mid
    
    if cut<m:
        end=mid-1
    else:
        start=mid+1

print(end)