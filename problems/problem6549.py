'''
코드 출처: https://hooongs.tistory.com/330
이 문제는 스택을 이용하는 방법과 세그먼트 트리, 분할 정복을 이용하는 방법이
존재하지만 이번 글에서는 스택을 이용하는 방법만 다뤄보겠습니다. 스택을 이용하는
방법이 시간복잡도도 O(N)에 가까우며 구현도 세그먼트 트리를 사용하는 방법보다
간단하다고 생각이 듭니다.
스택을 이용하는 방법의 원리는 간단합니다. 배열의 왼쪽에서부터 탐색을 시작해
스택에 최솟값에 대한 정보를 계속 유지해나가면서 스택의 가장 위의 값보다 작은
값이 나온다면 그 값들을 pop하면서 넓이들을 구해보며 넓이의 최댓값을 찾아나가는
것입니다.
'''

from collections import deque
import sys

while True:
    rec=list(map(int,sys.stdin.readline().split()))
    n=rec.pop(0)

    if n==0:
        break

    stack=deque()
    answer=0

    # 왼쪽부터 차례대로 탐색
    for i in range(n):
        while len(stack)!=0 and rec[stack[-1]]>rec[i]:
            tmp=stack.pop()

            if len(stack)==0:
                width=i
            else:
                width=i-stack[-1]-1
            answer=max(answer,width*rec[tmp])
        stack.append(i)

    # 스택에 남아 있는 것을 처리
    while len(stack)!=0:
        tmp=stack.pop()
        if len(stack)==0:
            width=n
        else:
            width=n-stack[-1]-1
        answer=max(answer,width*rec[tmp])

    print(answer)