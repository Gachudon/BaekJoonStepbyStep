s=input()
lc={}
for i in range(ord('a'),ord('z')+1):
    lc[i]=-1
for i in range(len(s)):
    if lc[ord(s[i])]!=-1:continue
    lc[ord(s[i])]=i
for i in range(ord('a'),ord('z')+1):
    print("%d "%lc[i],end='')
print()