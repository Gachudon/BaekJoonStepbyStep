import sys

input=sys.stdin.readline

def is666(n:int):
    if str(n).find('666')!=-1:
        return True
    else: return False

n=int(input())

cnt=0
i=0
while cnt<n:
    i+=1
    while not is666(i):
        i+=1
    cnt+=1

print(i)