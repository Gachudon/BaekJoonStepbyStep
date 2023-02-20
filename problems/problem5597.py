n=[]
for i in range(30):
    n.append(1)
for i in range(28):
    m=int(input())
    if m>30 or m<1:quit()
    if n[m-1]==0:quit()
    n[m-1]=0

for i in range(30):
    if n[i]==1:print(i+1)