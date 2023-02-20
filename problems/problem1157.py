s=input()
s = s.upper()
apb ={}
for i in s:
    if i in apb:
        apb[i]+=1
    else: apb[i]=1
max=0
for i in apb:
    if max<apb.get(i):max=apb.get(i)
maxa=''
for i in apb:
    if max==apb.get(i):
        if maxa!='':
            maxa='?'
            break
        else:
            maxa=i
print(maxa)