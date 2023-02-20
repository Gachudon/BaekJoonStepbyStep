def solve(a:list):
    if len(a)>3000000 or len(a)<1:quit()
    ans=0
    for i in range(len(a)):
        if a[i]>1000000 or a[i]<0:quit()
        ans+=a[i]
    return ans

a=[]
for i in range(100):
    a.append(i)
b = solve(a)
print(b)