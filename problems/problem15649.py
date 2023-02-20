import sys

input=sys.stdin.readline

n,m=map(int,input().split())

s=[] # 재귀함수를 이용하여 m개의 수열을 저장하기 위한 리스트

def dfs():
    if len(s)==m: # 리스트에 들어간 수열들이 m개가 되면 리스트에 들어있는 숫자들을 모두 출력하고 함수를 나온다.
        print(' '.join(map(str,s)))
        return
    
    for i in range(1,n+1):
        if i not in s: # 리스트 s 중복 확인
            s.append(i) # 중복이 아니면 숫자 i 를 리스트 s에 넣기
            dfs() #현재 s=[1]인 상태에서 다음 숫자를 넣기 위하여 가지치기하기(재귀함수)
            s.pop()

dfs()

# 코드 출처: https://jiwon-coding.tistory.com/21