'''
코드 출처: https://claude-u.tistory.com/154
heap을 tuple로 구성했을 때, 맨 앞 숫자만 가지고 정렬하므로 앞은 abs(절대값)
내장 함수를 써주고 두 번째는 원래 수를 써줌으로써 절댓값 정렬을 할 수 있게
된다.
'''
import sys
import heapq

numbers=int(input())
heap=[]

for _ in range(numbers):
    num=int(sys.stdin.readline())
    if num!=0:
        heapq.heappush(heap,(abs(num),num))
    else:
        try:
            print(heapq.heappop(heap)[1])
        except:
            print(0)

# from sys import stdin
# input=stdin.readline

# n=int(input())
# heap=[0]

# for _ in range(n):
#     num=int(input())
#     if num==0:
#         try:
#             print(heap[1])
#             heap[1]=heap.pop()
#         except:
#             print(0)
#     else:
#         try:
#             a
#         except:
#             a