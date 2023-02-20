import sys

input=sys.stdin.readline

k=int(input())
# 임의의 연속된 두 변을 곱하고, 그 두 변과 떨어진 연속된 두 변을 곱한다.
# 두 개의 곱이 작은 변 2개의 곱과 큰 변 2개의 곱이라면 그 두 곱을 차한다.
# 아니라면 두 곱을 합한다.
# 맞췄음

# s=[None]*6
# direction_dict={}
# for i in range(6):
#     s[i]=tuple(map(int,input().split()))
#     if s[i][0] in direction_dict:
#         direction_dict[s[i][0]]+=1
#     else:
#         direction_dict[s[i][0]]=1

# area=0
# area1=s[0][1]*s[1][1]
# area2=s[3][1]*s[4][1]
# if direction_dict[s[0][0]]==direction_dict[s[1][0]]==1:
#     area=area1-area2
# elif direction_dict[s[3][0]]==direction_dict[s[4][0]]==1:
#     area=area2-area1
# else:
#     area=area1+area2

# print(area*k)

'''
큰 사각형에서 작은 사각형을 빼면 ㄱ자 도형의 면적을 구할 수 있음.
큰 사각형의 면적은 주어진 변의 길이 중 가장 긴 가로변, 세로변의 길이를 구해서
곱하면 됨. 작은 사각형은 주어진 정보를 이용하여 가장 긴 가로변을 구할 수 있음.
(위에 큰 사각형의 면적을 구하기 위해서도 필요) 최장 가로변 양옆에는 두 개의
세로변이 위치함. 이 때 두 변의 차이를 구하면 우리가 구하고자 하는 작은 사각형의
세로변이 됨. 인접한 변의 길이는 배열에 담아 놨으므로 최장 가로변 인덱스-1, +1을
이용해서 찾아줄 수 있고, 최장 가로변이 어디에 위치하고 있을 지 알 수 없으므로
나머지 연산을 이용해서 인접한 변을 찾을 수 있도록 설정함
'''

import sys
input=sys.stdin.readline

melon=int(input()) # 참외수
arr=[list(map(int,input().split())) for _ in range(6)]
w=0; w_idx=0 # 가장 긴 가로변 길이, 인덱스 초기화
h=0; h_idx=0 # 가장 긴 세로변 길이, 인덱스 초기화
for i in range(len(arr)):
    if arr[i][0]==1 or arr[i][0]==2: # 방향이 동, 서면 가로
        if w<arr[i][1]: #가장 큰 값, 인덱스 찾기
            w=arr[i][1]
            w_idx=i
        elif arr[i][0]==3 or arr[i][0]==4:
            if h<arr[i][0]:
                h=arr[i][0]
                h_idx=i

# 가장 긴 가로변 양옆에 붙어있는 변(세로변)들의 차이 : 뺄 사각형의 세로
# 가장 긴 세로변 양옆에 붙어있는 변(가로변)들의 차이 : 뺄 사각형의 가로
subW=abs(arr[(w_idx-1)%6][1]-arr[(w_idx+1)%6][1])
subH=abs(arr[(h_idx-1)%6][1]-arr[(h_idx+1)%6][1])
ans=((w*h)-(subW*subH)*melon)
print(ans)