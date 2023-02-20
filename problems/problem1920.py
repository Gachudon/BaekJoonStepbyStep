'''
코드 출처: https://chancoding.tistory.com/44
이분 탐색 알고리즘에 따라서 데이터가 포함되어 있는 지 확인하는 풀이 방법을
사용했습니다.
1. 이분 탐색을 위해서 집합 N을 먼저 정렬시켰습니다.
2. 시작과 끝 지점의 index를 지정합니다.
3. 시작 인덱스와 끝 인덱스를 사용해서 중간 지점의 인덱스를 구합니다.
4. 중간 지점의 값과 element를 비교합니다.
    1. 동일한 값이면 찾았다!
    2. 값이 크다=> 중간보다 윗 부분에서 탐색
    3. 값이 작다=> 중간보다 작은 부분에서 탐색
    4. 위 과정을 확인할 리스트가 없을 때 까지 계속해서 반복한다.
5. 전체 리스트에서 확인이 불가능하면 없는 것으로 판별
'''

from sys import stdin, stdout
n=stdin.readline()
N=sorted(map(int,stdin.readline().split()))
m=stdin.readline()
M=map(int,stdin.readline().split())

def binary(l,N,start,end):
    if start>end:
        return 0
    m=(start+end)//2
    if l==N[m]:
        return 1
    elif l<N[m]:
        return binary(l,N,start,m-1)
    else:
        return binary(l,N,m+1,end)
    
for l in M:
    start=0
    end=len(N)-1
    print(binary(l,N,start,end))
# n=int(input())
# a=list(map(int,input().split()))
# m=int(input())
# f=list(map(int,input().split()))
# # a=[1,2,3,4]
# # try:
# #     a.index(5)
# # except:
# #     print(0)

# for i in range(m):
#     try:
#         if a.index(f[i])>=0:
#             print(1)
#     except:
#         print(0)