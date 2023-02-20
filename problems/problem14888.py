# import sys

# input=sys.stdin.readline

# n=int(input())
# a=list(map(int,input().split()))
# op=list(map(int,input().split()))
# min=1000000000
# max=-1000000000


# def dfs():
#     global op
#     if op[0]==op[1]==op[2]==op[3]==0:

'''
코드 출처: https://velog.io/@kimdukbae/BOJ-14888-%EC%97%B0%EC%82%B0%EC%9E%90-%EB%81%BC%EC%9B%8C%EB%84%A3%EA%B8%B0-Python
1. 연산자들에 대한 순열을 구하여 푸는 방법.
    파이썬 permutations 모듈을 이용하여 모든 순열을 구하여 완전탐색을 수행하면
    된다. 완전탐색의 경우 Python3에서 시간초과가 나므로 PyPy3로 제출해야 한다.
2. DFS를 이용해 최대, 최솟값을 구하는 방법.
    DFS의 경우 Python3에서 통과가 된다. DFS 풀이는 연산자의 갯수만큼 탐색을
    하며, 연산자가 존재하면 그 연산을 수행하며 재귀호출을 통해 탐색을 진행한다.

문제에서 주의할 점은 우선순위를 무시하고 무조건 앞에서부터 연산을 진행해야 한다.
또, 나눗셈은 정수 나눗셈으로 몫만 취하며, 음수를 양수로 나눌 때는 양수로 바꾼
뒤 몫을 취하고, 그 몫을 음수로 바꾼 것과 같다는 점이다.
'''

# 백트래킹(DFS)
import sys

input = sys.stdin.readline
N = int(input())
num = list(map(int, input().split()))
op = list(map(int, input().split()))  # +, -, *, //

maximum = -1e9
minimum = 1e9


def dfs(depth, total, plus, minus, multiply, divide):
    global maximum, minimum
    if depth == N:
        maximum = max(total, maximum)
        minimum = min(total, minimum)
        return

    if plus:
        dfs(depth + 1, total + num[depth], plus - 1, minus, multiply, divide)
    if minus:
        dfs(depth + 1, total - num[depth], plus, minus - 1, multiply, divide)
    if multiply:
        dfs(depth + 1, total * num[depth], plus, minus, multiply - 1, divide)
    if divide:
        dfs(depth + 1, int(total / num[depth]), plus, minus, multiply, divide - 1)


dfs(1, num[0], op[0], op[1], op[2], op[3])
print(maximum)
print(minimum)

'''
# 순열
import sys
from itertools import permutations

input=sys.stdin.readline
N=int(input())
num=list(map(int,input().split()))
op_num=list(map(int,input().split())) # +, -, *, //
op_list=['+','-','*','/']
op=[]

for k in range(len(op_num)):
    for i in range(op_num[k]):
        op.append(op_list[k])

maximum=-1e9
mimimum=1e9

def solve():
    global maximum, minimum
    for case in permutations(op,N-1):
        total=num[0]
        for r in range(1,N):
            if case[r-1]=='+':
                total+=num[r]
            elif case[r-1]=='-':
                total-=num[r]
            elif case[r-1]=='/':
                total=int(total/num[r])

        if total>maximum:
            maximum=total
        if total<minimum:
            minimum=total

solve()
print(maximum)
print(minimum)
'''