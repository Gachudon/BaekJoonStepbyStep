import sys
input=sys.stdin.readline

n=int(input())
arr=[None]*n
for i in range(n):
    arr[i]=tuple(map(int,input().split()))
r=[1]*n

for i in range(n):
    for j in range(n):
        if arr[i][0]<arr[j][0] and arr[i][1]<arr[j][1]:
            r[i]+=1

for i in r:
    print(i,end=' ')
print()