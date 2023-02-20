t=int(input())
f=[]
for i in range(t):
    k=int(input())
    if k>14 or k<1:quit()
    n=int(input())
    if n>14 or n<1:quit()
    f.append(1)
    for j in range(k+1):
        f[i]=int(f[i]*(n+j)/(j+1))

for i in range(t):
    print(f[i])