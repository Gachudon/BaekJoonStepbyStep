n=[]
for i in range(10):
    n.append(int(input()))
    if n[i]>1000 or n[i]<0:quit()
remainder = set()
for i in range(10):
    remainder.add(n[i]%42)
print(len(remainder))