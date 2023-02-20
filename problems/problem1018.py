import sys

input=sys.stdin.readline

# n,m=map(int,input().split())
# min = 33
# chess=[None]*n
# for i in range(n):
#     chess[i]=input().replace('\n','')
#     if len(chess[i])!=m:quit()

# for i in range(n-7):
#     for j in range(m-7):
#         cnt=0
#         stack=[]
#         for k in range(i,i+8):
#             for p in range(j,j+8):
#                 if len(stack)==0 or stack[-1]==chess[k][p]:
#                     stack.append(chess[k][p])
#                 elif stack[-1]!=chess[k][p] or p==j+7:
#                     cnt+=len(stack)//2
#                     stack=[]
#         if min>cnt:min=cnt
#         # print(cnt)

# print(min)

'''
코드 출처: https://bambbang00.tistory.com/43
N*M 보드를 map() 함수를 이용하여 띄어쓰기로 구분하여 입력 받는다.
원래의 판을 저장하기 위한 리스트 original과
바뀐 체스판의 갯수를 저장하기 위한 리스트 count를 정의한다.
N(행)의 갯수만큼 원래의 판을 입력 받는다.
original이 리스트 이므로 append(input())을 이용하여 리스트에 추가 해준다.
'''
N,M=map(int,input().split())
original=[]
count=[]

for _ in range(N):
    original.append(input().replace('\n',''))

'''
가능한 모든 경우의 수를 체크하기 위해 4중 for문을 사용한다.
첫번째, 두번째 for문은 전체 체스판에서 시작점을 잡기 위한 반복문이다.
a는 행, b는 열에 대하여 원래의 체스 판에서 8*8로 자를 수 있는 범위의 시작점을
가리킨다.
index1은 'W'로 시작할 경우 바뀐 체스 판의 갯수를 세기 위함이고,
index2는 'B'로 시작할 경우 바뀐 체스 판의 갯수를 세기 위함이다.
'''

for a in range(N-7):
    for b in range(M-7):
        index1=0
        index2=0
        '''
        행과 열의 시작점 a,b를 기준으로 8칸씩 모두 체크한다.
        현재 행의 번호 i, 현재 열의 번호 j의 합이 짝수이면 시작점의 색깔과
        같아야 하고, 홀수이면 시작점의 색깔과 다른 색이어야 한다. 이를 이용하여
        만약 (i+j)의 합이 짝수 일 경우, W가 아니라면 index1에 1을 더하고,
        B가 아니라면 index2에 1을 더한다. else문은 (i+j)의 합이 홀수인 경우로,
        시작점의 색깔과 다르지 않은 경우를 체크한다.
        '''
        for i in range(a,a+8):
            for j in range(b,b+8):
                if (i+j)%2==0:
                    if original[i][j]!='W':
                        index1+=1
                    if original[i][j]!='B':
                        index2+=1
                else:
                    if original[i][j]!='B':
                        index1+=1
                    if original[i][j]!='W':
                        index2+=1
    '''
    'W'로 시작할 경우와 'B'로 시작할 경우 바뀐 체스판의 수 중 작은 수를
    count 리스트에 더해준다. 모든 경우의 수를 다 체크한 후, count 중 제일 작은
    수를 출력하고 프로그램을 종료한다.
    '''
    count.append(min(index1,index2))

print(min(count))