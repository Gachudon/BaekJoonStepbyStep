max=0
n=[]
idx=0
for i in range(9):
    n.append(int(input()))
    if max<n[i]:
        max=n[i]
        idx=i+1
print(max)
print(idx)