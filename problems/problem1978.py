n=int(input())
if n>100 or n<1:quit()
cnt=0
num=list(map(int,input().split()))
if len(num)!=n:quit()
for i in range(n):
    if num[i]>1000 or num[i]<1:quit()
    isprime=True
    if num[i]==1:isprime=False
    else:
        for j in range(2,num[i]):
            if num[i]%j==0:isprime=False
    if isprime:cnt+=1
print(cnt)