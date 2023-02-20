n=int(input())
if n>1000 or n<1:quit()
ary=[]
for i in range(n):
    num=int(input())
    if num>1000 or num<-1000 or num in ary:quit()
    ary.append(num)
ary.sort()
for i in ary:
    print(i)