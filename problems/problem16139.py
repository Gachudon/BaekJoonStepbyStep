from sys import stdin
input=stdin.readline

s=input().rstrip()
arr=[[0]*26]
arr[0][ord(s[0])-97]=1
for i in range(1,len(s)):
    arr.append(arr[-1][:])
    arr[i][ord(s[i])-97]+=1

for _ in range(int(input())):
    c,start,end=list(input().split())
    start,end=map(int,[start,end])
    if start==0:
        print(arr[end][ord(c)-97])
    else:
        print(arr[end][ord(c)-97]-arr[start-1][ord(c)-97])
'''
코드 출처: https://my-coding-notes.tistory.com/551
범위를 입력받을 때 마다 문자의 처음부터 끝까지 알파뱃의 개수를 센다면 O(N^2)이
된다. 1억번 연산에 보통 1초가 소요된다고 하는데, 2,000,000^2는 400억이므로
시간 초과가 발생하게 된다. 따라서 문자열의 길이만큼 해당하는 dp 배열을 만들고
해당 구간까지의 알파벤이 총 몇 개였는 지 세둘 것이다. 그 후, 입력받은 범위의
알파벳 개수를 arr[r]-arr[l-1]로 O(1)로 구한다.
'''

# s=input().rstrip()
# if len(s)>2000:quit()
# q=int(input())
# if q>2000 or q<1:quit()