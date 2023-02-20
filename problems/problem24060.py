# def merge_sort(ary):
#     if len(ary)<2:
#         return ary
#     mid=len(ary)//2
#     low_arr=merge_sort(ary[:mid])
#     high_arr=merge_sort(ary[mid:])
#     merged_arr=[]
#     l=h=0
#     while 1<len(low_arr) and h<len(high_arr):
#         if low_arr[l]<high_arr[h]:
#             merged_arr.append(low_arr[l])
#             l+=1
#         else:
#             merged_arr.append(high_arr[h])
#             h+=1
#         merged_arr+=low_arr[l:]
#         merged_arr+=high_arr[h:]
#         return merged_arr

'''
코드 출처: https://my-coding-notes.tistory.com/581?category=957026
병합 정렬을 구현한 뒤, 데이터의 이동 순서를 기록하는 로직을 추가한다.
병합 정렬이 끝나면 기록된 순서의 k번째에 해당하는 수를 출력한다.
필자는 merge_sort와 merge를 따로 분리하진 않았다.

주의할 것이 있는데, 문제에선 4 5 1 3 2 와 같이 홀수인 경우를 병합할 때
45 132 가 아닌 451 32와 같이 앞이 크도록 병합하기 때문에 가운데 기준을
맞춰주는 mid 변수에 1을 더해준 뒤 2로 나누도록 했다.
'''

import sys
input=sys.stdin.readline

def merge_sort(L):
    if len(L)==1: return L

    mid=(len(L)+1)//2
    left=merge_sort(L[:mid])
    right=merge_sort(L[mid:])

    i,j=0,0
    L2=[]
    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            L2.append(left[i])
            ans.append(left[i])
            i+=1
        else:
            L2.append(right[j])
            ans.append(right[j])
            j+=1

    while i<len(left):
        L2.append(left[i])
        ans.append(left[i])
        i+=1
        
    while j<len(right):
        L2.append(right[j])
        ans.append(right[j])
        j+=1
    
    return L2

n, k = map(int,input().split())
a = list(map(int,input().split()))
ans=[]
merge_sort(a)
if len(ans)>=k:
    print(ans[k-1])
else:
    print(-1)