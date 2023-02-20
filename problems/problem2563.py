whitepaper=[[0 for col in range(100)] for row in range(100)]
for i in range(int(input())):
    l,b=map(int,input().split())
    if l>90 or l<0 or b>90 or b<0:quit()
    for j in range(l,l+10):
        for k in range(b,b+10):
            whitepaper[j][k]+=1

area=0
for i in range(100):
    for j in range(100):
        if whitepaper[i][j]>0:area+=1
print(area)