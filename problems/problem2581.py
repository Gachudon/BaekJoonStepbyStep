m=int(input())
if m>10000 or m<1:quit()
n=int(input())
if n>10000 or n<m:quit()
prime_num=[]

for i in range(m,n+1):
    if i%2==0 and i!=2 or i==1:continue
    else:
        isprime=True
        for j in range(3,int(i/2),2):
            if i%j==0:
                isprime=False
                break
        if isprime:
            prime_num.append(i)

sum=0
if len(prime_num)>0:
    for i in prime_num:
        sum+=i
    print(sum)
    print(prime_num[0])
else:print(-1)