'''
코드 출처: https://claude-u.tistory.com/267
1. array라는 리스트에 집들의 좌표를 입력받은 후에 정렬.
2. start=1,end=array[-1]-array[0]으로 설정.(시작 값은 최소 거리, 끝 값은
최대 거리)
3. 앞 집부터 공유기 설치
4. 설치를 할 수 있는 공유기 개수가 c개를 넘어가면 더 넓게 설치할 수 있다는
이야기 이므로 설치거리를 mid+1로 설정하여 다시 앞집부터 설치.
5. c개를 넘어가지 않는다면 더 좁게 설치해야 한다는 이야기 이므로 mid-1로 설정.

위의 과정을 반복 실행하면 정답을 얻을 수 있다.
'''
from sys import stdin
input=stdin.readline

n, c = map(int, input().split())

array = []
for i in range(n):
    array.append(int(input()))

array.sort()


def binary_search(array, start, end):
    while start <= end:
        mid = (start + end) // 2
        current = array[0]
        count = 1

        for i in range(1, len(array)):
            if array[i] >= current + mid:
                count += 1
                current = array[i]

        if count >= c:
            global answer
            start = mid + 1
            answer = mid
        else:
            end = mid - 1


start = 1
end = array[-1] - array[0]
answer = 0

binary_search(array, start, end)
print(answer)

# from sys import stdin
# input=stdin.readline

# n,c=map(int,input().split())
# line=[0]*n
# for i in range(n):
#     line[i]=int(input())

# line.sort()
# start=min(line)
# end=max(line)
# distance=(start+end)//(c-1)
# p=distance