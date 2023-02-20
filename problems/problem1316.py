n = int(input())
if n>100 or n<1:quit()
grword=[]
isgrword=[]
for i in range(n):
    s=input()
    if len(s)>100 or len(s)<1:quit()
    grword.append(set())
    isgrword.append(True)
    tmp=''
    for j in s:
        if j not in grword[i]:
            grword[i].add(j)
            tmp=j
        elif j in grword[i] and tmp!=j:
            isgrword[i]=False
            break
        else:tmp=j

cnt=0
for i in range(n):
    if isgrword[i]:cnt+=1
print(cnt)