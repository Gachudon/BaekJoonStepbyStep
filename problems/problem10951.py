sum=[]
while True:
    try:
        a,b=map(int,input().split())
    except:break
    if a>=10 or a<=0 or b>=10 or b<=0:quit()
    sum.append(a+b)

for i in range(len(sum)):print(sum[i])