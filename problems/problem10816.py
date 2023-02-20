import sys

input=sys.stdin.readline

n=int(input())
tmp=list(map(int,input().split()))
num_dict={}
for i in tmp:
    if i in num_dict:
        num_dict[i]+=1
    else:
        num_dict[i]=1

m=int(input())

tmp=list(map(int,input().split()))
for i in range(m):
    if tmp[i] in num_dict:
        tmp[i]=num_dict[tmp[i]]
    else:
        tmp[i]=0
    print(tmp[i],end=' ')

print()