'''
코드 출처: https://alpyrithm.tistory.com/134
도시의 개수와 도로의 길이, 주유소의 리터당 가격을 n,roads,costs에 입력받는다.
두 번째 도시로 가기 위해서 무조건 첫 번째에서 주유를 해야 한다.
첫 번째에서 두 번째 도시로 가는 도로의 길이 * 첫 번째 도시에서의 주유소의
리터당 가격을 더한다.
for문을 돌면서 지금까지 주유 가격보다 이번 도시에서의 가격이 작으면 지금까지
왔던 거리*가장 작았던 주유 가격을 곱해서 결과에 더해준다.
그리고 주유 가격을 제일 작은 가격으로 바꾼다.
마지막 도로에서 넘어갈 때 가격을 계산한다.
'''

n=int(input())
roads=list(map(int,input().split()))
costs=list(map(int,input().split()))

res=roads[0]*costs[0]
m=costs[0]
dist=0
for i in range(1,n-1):
    if costs[i]<m:
        res+=m*dist
        dist=roads[i]
        m=costs[i]
    else:
        dist+=roads[i]
    if i==n-2:
        res+=m*dist
print(res)

# n=int(input())
# if n>1000 or n<2:quit()

# road=list(map(int,input().split()))
# if sum(road)>10000:quit()

# oil=list(map(int,input().split()))
# for i in oil:
#     if i>10000:quit()

# cost=0
# i=0
# while i<n-1:
#     length=0
#     j=i+1
#     for j in j<n:
#         # print(i,j)
#         if oil[i]>oil[j]:
#             length+=road[j-1]
#             # cost+=length*oil[i]
#             # # print(cost)
#             # i=j
#             # print(i,j)
#             break
#         else:
#             length+=road[j-1]
#     cost+=length*oil[i]
#     i=j

# print(cost)