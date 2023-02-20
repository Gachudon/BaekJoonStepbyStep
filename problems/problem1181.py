import sys

n=int(sys.stdin.readline())
if n>20000 or n<1:quit()
arr=set()
for i in range(n):
    tmp=sys.stdin.readline().replace('\n','')
    if len(tmp)>50:quit()
    arr.add((tmp,len(tmp)))

arr=list(arr)
arr=sorted(arr,key=lambda x:x[0])
arr=sorted(arr,key=lambda x:x[1])
for i in arr:
    print(i[0])