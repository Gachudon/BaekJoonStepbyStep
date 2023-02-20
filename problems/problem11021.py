t = int(input())
sum = []
for i in range(t):
    a,b = map(int,input().split())
    if a>=10 or a<=0 or b>=10 or b<=0:quit()
    sum.append(a+b)

for i in range(t):
    print("Case #%d: %d"%(i+1,sum[i]))