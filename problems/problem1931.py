from sys import stdin
input=stdin.readline

n=int(input())
meeting=[tuple(map(int,input().split())) for _ in range(n)]
meeting=sorted(meeting,key=lambda x:x[0])
meeting=sorted(meeting,key=lambda x:x[1])
end=meeting[0][1]
count=1
for i in range(1,n):
    if end <= meeting[i][0]:
        end=meeting[i][1]
        count+=1
print(count)