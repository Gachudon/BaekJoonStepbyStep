# n=int(input())
# if n>1000000 or n<1:quit()
# arr=list(map(int,input().split()))
# if len(arr)!=n:quit()
# tmp=set(arr)
# tmp1=list(tmp)
# tmp1.sort(reverse=True)
# for i in range(len(tmp1)):
#     for j in range(len(arr)):
#         if arr[j]==tmp1[i]: arr[j]=len(tmp1)-i-1
# for i in arr:
#     print("%d "%i,end='')
# print()

'''
코드 출처: https://gudwns1243.tistory.com/52
풀이 자체는 어렵지 않았다.
set함수를 통해 중복을 없애준 후 정렬시킨 새로운 리스트를 만들어 준 후에
arr를 순서대로 돌면서 새로만든 arr2에서 해당 값의 인덱스를 뽑아주면 되는 문제였다.
하지만 시간초과가 떠서 조금 고민하게 만들었는데, 시간복잡도에 대한 고려를
해주지 않은게 그 원인이었다. list.index(i)의 형태는 시간복잡도 O(N)을
가지고 있고 그렇다면 매번 최대 1,000,000번의 수행이 이루어지게 돼서 
시간초과가 나는 것이었다. 때문에 이를 해결하기 위해 dict를 사용하기로 했다.

{ dict[요소] : 요소의 index }의 형태로 저장해 줌으로써
dict[i]의 형태로 시간복잡도 O[1]로 답을 뽑을 수 있게 하였고 문제를 통과했다.
'''

import sys

n=int(input())
arr=list(map(int,input().split()))

arr2=sorted(list(set(arr)))
dic={arr2[i]:i for i in range(len(arr2))}
for i in arr:
    print(dic[i],end=' ')
print()