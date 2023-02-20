n=int(input())
if n>100 or n<0:quit()
tmp=n
cnt=0
while True:
    tmp1 = int(tmp/10) + tmp%10
    tmp = (tmp%10)*10 +tmp1%10
    cnt+=1
    if tmp==n:break
print(cnt)