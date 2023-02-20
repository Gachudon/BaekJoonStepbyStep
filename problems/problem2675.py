t = int(input())
if t>1000 or t<1:quit()
out=[]
for i in range(t):
    r,s=map(str,input().split())
    r=int(r)
    if r>8 or r<1:quit()
    if len(s)>20 or len(s)<1:quit()
    out.append('')
    for j in s:
        for k in range(r):
            out[i]+=j
for i in range(t):print(out[i])