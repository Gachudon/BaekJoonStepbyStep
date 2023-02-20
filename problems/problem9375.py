# 딕셔너리로 입력을 받는다.
# C라면 스트럭트로 받는다.

import sys
input=sys.stdin.readline

t=int(input())
ans=[0]*t
for i in range(t):
    part_dict={}
    for _ in range(int(input())):
        costume, part=input().split()
        if part in part_dict:
            part_dict[part]+=1
        else:
            part_dict[part]=1
    tmp=1
    for j in part_dict.values():
        tmp*=j+1
    ans[i]+=tmp-1


for i in ans:
    print(i)

'''
코드 출처: https://hongcoding.tistory.com/60
같은 종류의 의상은 하나씩만 착용할 수 있으며, 알몸이 아니어야 하므로 꼭 1종류
이상의 의상은 착용해야 한다.

그렇다면 다음과 같은 식을 세울 수 있다.
(a 종류수+1)*(b 종류수+1)*(c 종류수+1)...-1

여기서 종류수에 +1을 해준 이유는 그 종류의 의상을 착용해도 되고 안해도 되기
때문이고 마지막에 -1을 해준 이유는 모든 의상을 착용하지 않은 경우를
제외시켜줘야 하기 때문이다.
'''