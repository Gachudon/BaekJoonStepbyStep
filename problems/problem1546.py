n = int(input())
score = list(map(float,input().split()))
if len(score)!=n:quit()
zeros=0
for i in range(n):
    if score[i]>100 or score[i]<0:quit()
    if score[i]==0:zeros+=1
if zeros==n:quit()
max=0
for i in range(n):
    if max<score[i]:max=score[i]
sum=0
for i in range(n):
    score[i]=score[i]/max*100
    sum+=score[i]
print(sum/n)