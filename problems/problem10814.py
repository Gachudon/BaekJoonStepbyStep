import sys

n=int(sys.stdin.readline())
if n>100000 or n<1:quit()

arr=[None]*n
for i in range(n):
    age,name=map(str,sys.stdin.readline().replace('\n','').split())
    age=int(age)
    if age>200 or age<1 or len(name)>100:quit()
    arr[i]=(age,name,i)

arr=sorted(arr,key=lambda x:x[2])
arr=sorted(arr,key=lambda x:x[0])

for i in arr:
    print(i[0],i[1])